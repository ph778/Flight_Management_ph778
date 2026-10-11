import sqlite3

db_name = "DBName.db"

def create_table_airports(db_name):
    create_table = "CREATE TABLE airports (apCode VARCHAR(3) NOT NULL PRIMARY KEY, city VARCHAR(20), country VARCHAR(20));"

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table)

        conn.commit()
        print(f"Table 'airports' created in DBName.db")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

def import_data_airports(db_name):
    import_data = [
        ("LHR","London","UK"),
        ("YVR","Vancouver","Canada"),
        ("YUL","Montreal","Canada"),
        ("HND","Tokyo","Japan"),
        ("HAN","Hanoi","Vietnam"),
        ("BRS","Bristol","UK"),
        ("LYN","Lyon","France"),
        ("HAM","Hamburg","Germany")
    ]

    conn = None
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO airports (apCode, city, country) VALUES (?, ?, ?)", import_data
        )

        conn.commit()
        print(f"Data inserted into airports")

    except Exception as e:
            print(e)
    
    finally:
        if conn:
            conn.close()


def create_table_aircraft(db_name):
    create_table = "CREATE TABLE aircraft (type VARCHAR(4) NOT NULL PRIMARY KEY, manufacturer VARCHAR(20), model VARCHAR(20) NOT NULL, capacity INT, longhaul BOOLEAN);"

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table)

        conn.commit()
        print(f"Table 'aircraft' created in DBName.db")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

def import_data_aircraft(db_name):
    import_data = [
        ('A20N','Airbus','A320neo','240','FALSE'),
        ('B737','Boeing','737-700','120','FALSE'),
        ('A359','Airbus','A350-900','325','TRUE')

    ]

    conn = None
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO aircraft (type, manufacturer, model, capacity, longhaul) VALUES (?, ?, ?, ?, ?)", import_data
        )

        conn.commit()
        print(f"Data inserted into aircraft")

    except Exception as e:
            print(e)
    
    finally:
        if conn:
            conn.close()

def create_table_pilots(db_name):
    create_table = "CREATE TABLE pilots (idPilot INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, idEmployee INT NOT NULL, first_name VARCHAR(20), surname VARCHAR(20), captain BOOLEAN, active BOOLEAN);"

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table)

        conn.commit()
        print(f"Table 'pilots' created in DBName.db")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

def import_data_pilots(db_name):
    import_data = [
        ('001','51430','Vance','Sterling','TRUE','TRUE'),
        ('002','30516','Amara','Vance','TRUE','TRUE'),
        ('003','19785','Leo','Cross','TRUE','TRUE'),
        ('004','89000','Maya','Lin','TRUE','TRUE'),
        ('005','34697','Jaques','Mercier','TRUE','TRUE'),
        ('006','16430','Zane','Castillo','TRUE','FALSE'),
        ('007','75015','Kenji','Sato','FALSE','TRUE'),
        ('008','96759','Mateo','Silva','FALSE','TRUE'),
        ('009','89469','Priya','Nair','FALSE','TRUE'),
        ('010','75346','Lin','Wei','FALSE','TRUE'),
        ('011','34687','Zayn','Hashmi','FALSE','TRUE'),
        ('012','34698','Jessica','Tucker','FALSE','FALSE')
    ]

    conn = None
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO pilots (idPilot, idEmployee, first_name, surname, captain, active) VALUES (?, ?, ?, ?, ?, ?)", import_data
        )

        conn.commit()
        print(f"Data inserted into pilots")

    except Exception as e:
            print(e)
    
    finally:
        if conn:
            conn.close()

def create_table_airframes(db_name):
    create_table = "CREATE TABLE airframes (registration VARCHAR(6) NOT NULL PRIMARY KEY, serial INT, type VARCHAR(4) NOT NULL, introduced TEXT, hours INT, location VARCHAR(3) NOT NULL, active BOOLEAN, FOREIGN KEY (type) REFERENCES aircraft(type) ON DELETE CASCADE, FOREIGN KEY (location) REFERENCES airports(apCode));"

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table)

        conn.commit()
        print(f"Table 'airframes' created in DBName.db")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

def import_data_airframes(db_name):
    import_data = [
        ('G-TTNA','255','A20N','2016','28000','LYN','TRUE'),
        ('G-TTNE','256','A20N','2016','30250','HAM','TRUE'),
        ('G-TTNF','289','A20N','2017','31150','BRS','TRUE'),
        ('G-TTNJ','325','A20N','2018','34500','BRS','TRUE'),
        ('G-JPKA','10567','B737','1999','81500','BRS','FALSE'),
        ('G-JPKB','10602','B737','1999','89900','BRS','FALSE'),
        ('G-XWBA','359','A359','2013','33000','LHR','TRUE'),
        ('G-XWBB','360','A359','2013','34500','YVR','TRUE'),
        ('G-XWBC','361','A359','2013','35050','LHR','FALSE'),
        ('G-XWBG','362','A359','2014','28750','YVR','TRUE'),
        ('G-XWBH','363','A359','2014','26600','LHR','TRUE'),
        ('G-XWBI','364','A359','2015','24500','LHR','TRUE')
    ]

    conn = None
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO airframes (registration, serial, type, introduced, hours, location, active) VALUES (?, ?, ?, ?, ?, ?, ?)", import_data
        )

        conn.commit()
        print(f"Data inserted into airframes")

    except Exception as e:
            print(e)
    
    finally:
        if conn:
            conn.close()

def create_table_routes(db_name):
    create_table = "CREATE TABLE routes (idRoute INTEGER PRIMARY KEY AUTOINCREMENT, pointA VARCHAR(3) NOT NULL, pointB VARCHAR(3) NOT NULL, route_uq VARCHAR(6) UNIQUE, duration INT NOT NULL, active BOOLEAN, FOREIGN KEY (pointA) REFERENCES airport(apCode) ON DELETE CASCADE, FOREIGN KEY (pointB) REFERENCES airports(apCode) ON DELETE CASCADE);"

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table)

        conn.commit()
        print(f"Table 'routes' created in DBName.db")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

def import_data_routes(db_name):
    import_data = [
        ('0010','LHR','YVR','LHRYVR','570','TRUE'),
        ('0011','YVR','LHR','YVRLHR','570','TRUE'),
        ('0020','LHR','YUL','LHRYUL','450','TRUE'),
        ('0021','YUL','LHR','YULLHR','450','TRUE'),
        ('0030','LHR','HND','LHRHND','820','TRUE'),
        ('0031','HND','LHR','HNDLHR','820','TRUE'),
        ('0040','LHR','HAN','LHRHAN','720','FALSE'),
        ('0041','HAN','LHR','HANLHR','720','FALSE'),
        ('0050','BRS','LYN','BRSLYN','100','TRUE'),
        ('0051','LYN','BRS','LYNBRS','100','TRUE'),
        ('0060','BRS','HAM','BRSHAM','90','TRUE'),
        ('0061','HAM','BRS','HAMBRS','90','TRUE'),
        ('0070','HAM','LYN','HAMLYN','110','TRUE'),
        ('0071','LYN','HAM','LYNHAM','110','TRUE'),
        ('0080','HND','YVR','HNDYVR','530','TRUE'),
        ('0081','YVR','HND','YVRHND','530','TRUE')
    ]

    conn = None
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO routes (idRoute, pointA, pointB, route_uq, duration, active) VALUES (?, ?, ?, ?, ?, ?)", import_data
        )

        conn.commit()
        print(f"Data inserted into routes")

    except Exception as e:
            print(e)
    
    finally:
        if conn:
            conn.close()

def create_table_certifications(db_name):
    create_table = "CREATE TABLE certifications (idCertification INTEGER PRIMARY KEY AUTOINCREMENT, pilot INT NOT NULL, type VARCHAR(4) NOT NULL, certification_uq VARCHAR(10) UNIQUE, FOREIGN KEY (pilot) REFERENCES pilots(idPilot) ON DELETE CASCADE, FOREIGN KEY (type) REFERENCES aircraft(type) ON DELETE CASCADE);"

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table)

        conn.commit()
        print(f"Table 'certifications' created in DBName.db")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

def import_data_certifications(db_name):
    import_data = [
        ('001','001','A20N','001A20N'),
        ('002','002','A20N','002A20N'),
        ('003','002','A359','002A359'),
        ('004','003','A20N','003A20N'),
        ('005','004','A20N','004A20N'),
        ('006','004','A359','004A359'),
        ('007','005','A20N','005A20N'),
        ('008','007','A20N','007A20N'),
        ('009','007','A359','007A359'),
        ('010','007','B737','007B737'),
        ('011','008','A359','008A359'),
        ('012','009','A20N','009A20N'),
        ('013','009','A359','009A359'),
        ('014','010','A20N','010A20N'),
        ('015','011','A20N','011A20N'),
        ('016','012','A359','012A359')
    ]

    conn = None
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO certifications (idCertification, pilot, type, certification_uq) VALUES (?, ?, ?, ?)", import_data
        )

        conn.commit()
        print(f"Data inserted into certifications")

    except Exception as e:
            print(e)
    
    finally:
        if conn:
            conn.close()

def create_table_flights(db_name):
    create_table = "CREATE TABLE flights (flight_number INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, designation VARCHAR(7), route INT NOT NULL, departure_time TEXT, longhaul BOOLEAN, arrival_time TEXT, airframe VARCHAR(6), crewed BOOLEAN, active BOOLEAN, FOREIGN KEY (route) REFERENCES routes(idRoute) ON DELETE CASCADE, FOREIGN KEY (airframe) REFERENCES airframes(registration));"

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table)

        conn.commit()
        print(f"Table 'flights' created in DBName.db")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

def import_data_flights(db_name):
    import_data = [
        ('057','JP-057','0020','2026-09-24 21:30','TRUE','2026-09-25 05:00','G-XWBB','TRUE','FALSE'),
        ('058','JP-058','0021','2026-09-25 16:30','TRUE','2026-09-26 00:00','G-XWBB','TRUE','FALSE'),
        ('059','JP-059','0010','2026-09-25 16:42','TRUE','2026-09-26 02:12','G-XWBB','TRUE','FALSE'),
        ('060','JP-060','0051','2026-09-25 18:39','FALSE','2026-09-25 20:19','G-TTNA','TRUE','TRUE'),
        ('061','JP-061','0081','2026-09-26 03:30','TRUE','2026-09-26 12:20','G-XWBG','TRUE','TRUE'),
        ('062','JP-062','0050','2026-09-26 08:15','FALSE','2026-09-26 09:55','G-TTNF','TRUE','TRUE'),
        ('063','JP-063','0060','2026-09-26 08:20','FALSE','2026-09-26 09:50','G-TTNJ','TRUE','TRUE'),
        ('064','JP-064','0060','2026-09-26 10:15','FALSE','2026-09-26 11:45','G-TTNA','TRUE','TRUE'),
        ('065','JP-065','0070','2026-09-26 10:15','FALSE','2026-09-26 12:05','G-TTNE','FALSE','TRUE'),
        ('066','JP-066','0061','2026-09-26 10:21','FALSE','2026-09-26 11:51','G-TTNJ','FALSE','TRUE'),
        ('067','JP-067','0061','2026-09-27 10:21','FALSE','2026-09-27 11:51','G-TTNA','FALSE','TRUE'),
        ('068','JP-068','0080','2026-09-29 00:00','TRUE','2026-09-29 13:40','G-XWBG','FALSE','TRUE')
    ]

    conn = None
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO flights (flight_number, designation, route, departure_time, longhaul, arrival_time, airframe, crewed, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", import_data
        )

        conn.commit()
        print(f"Data inserted into flights")

    except Exception as e:
            print(e)
    
    finally:
        if conn:
            conn.close()

def create_table_crews(db_name):
    create_table = "CREATE TABLE crews (idCrew INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, flight INT NOT NULL, captain INT NOT NULL, officer INT, reserve INT, FOREIGN KEY (flight) REFERENCES flights(flight_number) ON DELETE CASCADE, FOREIGN KEY (captain) REFERENCES pilots(idPilot) ON DELETE CASCADE, FOREIGN KEY (officer) REFERENCES pilots(idPilot), FOREIGN KEY (reserve) REFERENCES pilots(idPilot));"

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute(create_table)

        conn.commit()
        print(f"Table 'crews' created in DBName.db")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()

def import_data_crews(db_name):
    import_data = [
        ('00131','JP-057','002','009','005'),
        ('00132','JP-058','004','009','002'),
        ('00133','JP-059','005','012','008'),
        ('00134','JP-060','001','011',''),
        ('00135','JP-061','002','008','005'),
        ('00136','JP-062','003','009',''),
        ('00137','JP-063','001','011',''),
        ('00138','JP-064','004','007',''),
        ('00139','JP-065','005','010','')
    ]

    conn = None
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO crews (idCrew, flight, captain, officer, reserve) VALUES (?, ?, ?, ?, ?)", import_data
        )

        conn.commit()
        print(f"Data inserted into crews")

    except Exception as e:
            print(e)
    
    finally:
        if conn:
            conn.close()

##view all database data 

def view_db(db_name):
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

##create_table_airports(db_name)
##import_data_airports(db_name)

##create_table_aircraft(db_name)
##import_data_aircraft(db_name)

##create_table_pilots(db_name)
##import_data_pilots(db_name)

##create_table_airframes(db_name)
##import_data_airframes(db_name)

##create_table_routes(db_name)
##import_data_routes(db_name)

##create_table_certifications(db_name)
##import_data_certifications(db_name)

##create_table_flights(db_name)
##import_data_flights(db_name)

##create_table_crews(db_name)
##import_data_crews(db_name)

view_db(db_name)