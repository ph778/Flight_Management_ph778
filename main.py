import sqlite3

# named database object

db_name = "DBName.db"

# Define DBOperation class to manage all data into the database.

class DBOperations:
  
  def get_connection(self):
    self.conn = sqlite3.connect(db_name)
    self.cur = self.conn.cursor()

# menu for display by search variables

  def display_flights_routes_menu(self):

    while True:
      print("\n View Flights and Routes Menu:")
      print("**********")
      print(" 1. Display flights by Flight No.")
      print(" 2. Display flights by destination airport")
      print(" 3. Display routes by airport")
      print(" 4. Display routes by duration")
      print(" 5. Display all records from FlightInfo")
      print(" 6. Exit to Main\n")

      __choose_menu = int(input("Enter your choice: "))
      db_ops = DBOperations()
      if __choose_menu == 1:
        db_ops.search_flight_number()
      elif __choose_menu == 2:
        db_ops.search_flight_destination()
      elif __choose_menu == 3:
        db_ops.search_route_airport()
      elif __choose_menu == 4:
        db_ops.search_route_duration()
      elif __choose_menu == 5:
        db_ops.display_all()
      elif __choose_menu == 6:
        return
      else:
        print("Invalid Choice")

# displays all data within the database db_name, table by table

  def display_all(self):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = cursor.fetchall()
    
    if not tables:
      print("No tables found")
    
    else:
      for table_tuple in tables:
        table_name = table_tuple[0]
        print(f"\n=== Table: {table_name} ===")
    
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
    
        if not rows:
          print("Empty")
        else:
          for row in rows:
            print(row)
    
    conn.close()
       
# displays records matching the flight number entered

  def search_flight_number(self):
    try:
      self.get_connection()
      flight_number = int(input("Enter Flight No: "))
      self.cur.execute("SELECT * FROM flights WHERE flight_number = ?", (flight_number,))
      result = self.cur.fetchone()
      if isinstance(result, tuple):
        print("\nFlight found.........\n")
        for index, detail in enumerate(result):
          if index == 0:
            print("Flight Number: " + str(detail))
          elif index == 1:
            print("Flight Designation: " + detail)
          elif index == 2:
            print("Route Number: " + str(detail))
            self.cur.execute("SELECT pointA FROM routes WHERE idRoute = ?", (detail,))
            result_pointA = self.cur.fetchone()
            print("Departing: " + str(result_pointA[0]))
            self.cur.execute("SELECT pointB FROM routes WHERE idRoute = ?", (detail,))
            result_pointB = self.cur.fetchone()
            print("Arriving: " + str(result_pointB[0]))
          elif index == 3:
            print("Departure time: " + detail)
          elif index == 4:
            if detail == "TRUE":
              print("Long haul flight")
            else:
              print("Short haul flight")
            self.cur.execute("SELECT routes.duration FROM routes WHERE routes.idRoute = (SELECT flights.route FROM flights WHERE flight_number = ?)", (flight_number,))
            result_duration = self.cur.fetchone()
            print("Flight time: " + str(result_duration[0]) + " MIN")
          elif index == 5:
            print("Arrival time: " + detail)
          elif index == 6:
            print("Flying on: " + detail, end=" ")
            self.cur.execute("SELECT aircraft.manufacturer, aircraft.model FROM aircraft WHERE aircraft.type = (SELECT airframes.type FROM airframes WHERE airframes.registration = ?)", (detail,))
            result_aircraft = self.cur.fetchone()
            print(str(result_aircraft[0]) + " " + str(result_aircraft[1]))
          elif index == 7:
            if detail == "TRUE":
              print("Crew allocated:", end=" ")
              self.cur.execute("SELECT crews.idCrew, crews.captain, crews.officer FROM crews WHERE crews.flight = (SELECT flights.designation FROM flights WHERE flight_number = ?)", (flight_number,))
              result_crew_no = self.cur.fetchone()
              self.cur.execute("SELECT first_name, surname FROM pilots WHERE pilots.idPilot = (SELECT crews.captain FROM crews WHERE crews.idCrew = ?)", (result_crew_no[0],))
              result_captain = self.cur.fetchone()
              self.cur.execute("SELECT first_name, surname FROM pilots WHERE pilots.idPilot = (SELECT crews.officer FROM crews WHERE crews.idCrew = ?)", (result_crew_no[0],))
              result_officer = self.cur.fetchone()
              print("Crew Code: " + str(result_crew_no[0]) + ", Captain: " + str(result_captain[0]) + " " + str(result_captain[1]) + ", First Officer: " + str(result_officer[0]) + " " + str(result_officer[1]))
            else:
              print("Crew not yet allocated")          
          else:
            if detail == "TRUE":
              print("Flight status: active")
            else:
              print("Flight status: inactive")
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

# displays flights by destination airport

  def search_flight_destination(self):
    try:
      self.get_connection()
      destination_apcode = input("Enter Destination Airport Code: ").upper()
      self.cur.execute("SELECT * FROM flights WHERE flights.route IN (SELECT routes.idRoute FROM routes WHERE routes.pointB = ?)", (destination_apcode,))
            
      flights = self.cur.fetchall()

      if flights:
        print("\nFlights found.........\n")

        for result in flights:
          print("--------------------------------")
   
          for index, detail in enumerate(result):
            if index == 0:
              print("Flight Number: " + str(detail))
            elif index == 1:
              print("Flight Designation: " + detail)
            elif index == 2:
              print("Route Number: " + str(detail))
              self.cur.execute("SELECT pointA FROM routes WHERE idRoute = ?", (detail,))
              result_pointA = self.cur.fetchone()
              print("Departing: " + str(result_pointA[0]))
              self.cur.execute("SELECT pointB FROM routes WHERE idRoute = ?", (detail,))
              result_pointB = self.cur.fetchone()
              print("Arriving: " + str(result_pointB[0]))
            elif index == 3:
              print("Departure time: " + detail) 
            elif index == 4:
              print("", end="")     
            elif index == 5:
              print("Arrival time: " + detail)
            elif index == 6:
              print("Flying on: " + detail, end=" ")
              self.cur.execute("SELECT aircraft.manufacturer, aircraft.model FROM aircraft WHERE aircraft.type IN (SELECT airframes.type FROM airframes WHERE airframes.registration = ?)", (detail,))
              result_aircraft = self.cur.fetchone()
              print(str(result_aircraft[0]) + " " + str(result_aircraft[1]))
            elif index == 7:
              print("", end="")
            else:
              if detail == "TRUE":
                print("Flight status: active")
              else:
                print("Flight status: inactive")
          print()
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

# display routes by airport (either destination or departure)

  def search_route_airport(self):
      try:
        self.get_connection()
        route_apcode = input("Enter Airport Code: ").upper()
        self.cur.execute("SELECT * FROM routes WHERE routes.pointA = ? OR routes.pointB = ?", (route_apcode, route_apcode))
              
        routes = self.cur.fetchall()
  
        if routes:
          print("\nRoutes found.........\n")
  
          for result in routes:
            print("--------------------------------")
     
            for index, detail in enumerate(result):
              if index == 0:
                print("Route ID: " + str(detail))
              elif index == 1:
                self.cur.execute("SELECT city, country FROM airports WHERE apCode = ?", (detail,))
                result_airportA = self.cur.fetchone()
                print("Departure: "+ detail + ", " + str(result_airportA[0]) + ", " + str(result_airportA[1]))
              elif index == 2:
                self.cur.execute("SELECT city, country FROM airports WHERE apCode = ?", (detail,))
                result_airportB = self.cur.fetchone()
                print("Destination: "+ detail + ", " + str(result_airportB[0]) + ", " + str(result_airportB[1]))
              elif index == 3:
                print("", end="")     
              elif index == 4:
                print("Flight time: " + str(detail) + " MIN")
              else:
                if detail == "TRUE":
                  print("Route status: active")
                else:
                  print("Route status: inactive")
            print()
        else:
          print("No Record")
  
      except Exception as e:
        print(e)
      finally:
        self.conn.close()

# displays all routes below a input flight time

  def search_route_duration(self):
      try:
        self.get_connection()
        route_duration = int(input("Enter maximum flight minutes: "))
        self.cur.execute("SELECT * FROM routes WHERE routes.duration <= ?", (route_duration,))
              
        routes = self.cur.fetchall()
  
        if routes:
          print("\nRoutes found.........\n")
  
          for result in routes:
            print("--------------------------------")
     
            for index, detail in enumerate(result):
              if index == 0:
                print("Route ID: " + str(detail))
              elif index == 1:
                self.cur.execute("SELECT city, country FROM airports WHERE apCode = ?", (detail,))
                result_airportA = self.cur.fetchone()
                print("Departure: "+ detail + ", " + str(result_airportA[0]) + ", " + str(result_airportA[1]))
              elif index == 2:
                self.cur.execute("SELECT city, country FROM airports WHERE apCode = ?", (detail,))
                result_airportB = self.cur.fetchone()
                print("Destination: "+ detail + ", " + str(result_airportB[0]) + ", " + str(result_airportB[1]))
              elif index == 3:
                print("", end="")     
              elif index == 4:
                print("Flight time: " + str(detail) + " MIN")
              else:
                if detail == "TRUE":
                  print("Route status: active")
                else:
                  print("Route status: inactive")
            print()
        else:
          print("No Record")
  
      except Exception as e:
        print(e)
      finally:
        self.conn.close()

# displays all flights with a input pilot id allocated

  def search_pilot_schedule(self):
    try:
      self.get_connection()
      idPilot = int(input("Enter Pilot ID: "))
      self.cur.execute("SELECT * FROM flights WHERE flights.flight_number IN (SELECT crews.flight FROM crews WHERE crews.captain = ? OR crews.officer = ? OR crews.reserve = ?)", (idPilot, idPilot, idPilot))
      result = self.cur.fetchall()

      if result:
        print("\nFlight found.........\n")

        for flight_row in result:
          print("--------------------------------")

          for index, detail in enumerate(flight_row):
            if index == 0:
              print("Flight Number: " + str(detail))
            elif index == 1:
              print("Flight Designation: " + detail)
            elif index == 2:
              print("Route Number: " + str(detail))
              self.cur.execute("SELECT pointA FROM routes WHERE idRoute = ?", (detail,))
              result_pointA = self.cur.fetchone()
              print("Departing: " + str(result_pointA[0]))
              self.cur.execute("SELECT pointB FROM routes WHERE idRoute = ?", (detail,))
              result_pointB = self.cur.fetchone()
              print("Arriving: " + str(result_pointB[0]))
            elif index == 3:
              print("Departure time: " + detail)
            elif index == 4:
              if detail == "TRUE":
                print("Long haul flight")
              else:
                print("Short haul flight")
              self.cur.execute("SELECT routes.duration FROM routes WHERE routes.idRoute = (SELECT flights.route FROM flights WHERE flight_number = ?)", (flight_row[0],))
              result_duration = self.cur.fetchone()
              print("Flight time: " + str(result_duration[0]) + " MIN")
            elif index == 5:
              print("Arrival time: " + detail)
            elif index == 6:
              print("Flying on: " + detail, end=" ")
              self.cur.execute("SELECT aircraft.manufacturer, aircraft.model FROM aircraft WHERE aircraft.type = (SELECT airframes.type FROM airframes WHERE airframes.registration = ?)", (detail,))
              result_aircraft = self.cur.fetchone()
              print(str(result_aircraft[0]) + " " + str(result_aircraft[1]))
            elif index == 7:
              print("Crew allocated: " + detail)         
            else:
              if detail == "TRUE":
                print("Flight status: active")
              else:
                print("Flight status: inactive")
          print()
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

# The main function will parse arguments.
# These argument will be defined by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print("\n Main Menu:")
  print("**********")
  print(" 1. placeholder: Add Flight")
  print(" 2. View Flights and Routes by Criteria")
  print(" 3. placeholder: Update Flight")
  print(" 4. placeholder: Assign pilot to Crew")
  print(" 5. View Pilot Schedule")
  print(" 6. placeholder: Update Airports")
  print(" 7. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    print("placeholder")
  elif __choose_menu == 2:
    db_ops.display_flights_routes_menu()
  elif __choose_menu == 3:
    print("placeholder")
  elif __choose_menu == 4:
    print("placeholder")
  elif __choose_menu == 5:
    db_ops.search_pilot_schedule()
  elif __choose_menu == 6:
    print("placeholder")  
  elif __choose_menu == 7:
    exit(0)
  else:
    print("Invalid Choice")
