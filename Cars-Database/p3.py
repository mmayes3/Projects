import sqlite3


def create_db_and_table():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS Public_Passenger_Vehicle_Licenses_table (VehicleType text, Status text, Vehiclemake text, " \
          "Vehiclemodel text, Vehiclemodelyear int, Vehiclecolor text, Vehiclefuelsource text, " \
          "WheelchairAccessible text, City text, State text, ZipCode int )"
    cursor.execute(sql)
    cursor.close()


def add__data_to_database():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    with open("Public_Passenger_Vehicle_Licenses-1.csv", "r") as f:
        for line in f:
            if not line.startswith("Vehicle Type"):
                L = line.split(",")
                VehicleType = L[0]
                Status = L[1]
                VehicleMake = L[2]
                VehicleModel = L[3]
                VehicleModelYear = L[4]
                VehicleColor = L[5]
                VehicleFuelSource = L[6]
                WheelchairAccessible = L[7]
                C = L[8]
                State = L[9]
                ZIPCode = L[10]

                sql = "INSERT INTO Public_Passenger_Vehicle_Licenses_table (VehicleType, Status, Vehiclemake, " \
          "Vehiclemodel, Vehiclemodelyear, Vehiclecolor, Vehiclefuelsource, " \
          "WheelchairAccessible, City, State, ZipCode) VALUES (:VehicleType, :Status, :Vehiclemake, :Vehiclemodel, " \
                      ":Vehiclemodelyear, :Vehiclecolor, :Vehiclefuelsource, :WheelchairAccessible, :City, :State, :ZipCode )"
                cursor.execute(sql, {"VehicleType": VehicleType , "Status": Status, "Vehiclemake": VehicleMake, "Vehiclemodel": VehicleModel,
                                     "Vehiclemodelyear": VehicleModelYear, "Vehiclecolor": VehicleColor, "Vehiclefuelsource": VehicleFuelSource,
                                     "WheelchairAccessible": WheelchairAccessible, "City": C, "State": State, "ZipCode": ZIPCode})
                conn.commit()
    cursor.close()



def display_all_hybridfuel_base():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql3 = "SELECT COUNT(Vehiclefuelsource) FROM Public_Passenger_Vehicle_Licenses_table"
    sql4 = "SELECT COUNT(*) FROM Public_Passenger_Vehicle_Licenses_table WHERE Vehiclefuelsource = 'Hybrid'; "
    columns1 = cursor.execute(sql3).fetchone()[0]
    columns = cursor.execute(sql4).fetchone()[0]
    print(100*(columns/columns1))

def display_max_year():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql5 = "SELECT AVG(Vehiclemodelyear) FROM Public_Passenger_Vehicle_Licenses_table"
    col = cursor.execute(sql5).fetchone()[0]
    print(2018-col)
def display_vehical_models_count():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT COUNT(DISTINCT Vehiclemodel) FROM Public_Passenger_Vehicle_Licenses_table"
    Vehiclemodel_column = cursor.execute(sql)
    all_Vehicle_model = Vehiclemodel_column.fetchone()[0]
    print(all_Vehicle_model)

def display_most_common_vehical_model():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql7 = "SELECT `Vehiclemodel` FROM `Public_Passenger_Vehicle_Licenses_table` GROUP BY `Vehiclemodel` ORDER BY COUNT(*) DESC LIMIT 1; "
    C = cursor.execute(sql7).fetchone()[0]
    print(C)

def display_SECOND_most_common_CITY():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql19 = "SELECT `City` FROM `Public_Passenger_Vehicle_Licenses_table` WHERE City != 'CHICAGO' GROUP BY `City` ORDER BY COUNT(*) DESC; "
    D = cursor.execute(sql19).fetchone()[0]
    print(D)
def display__most_common_ZIP():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql20 = "SELECT `ZipCode` FROM `Public_Passenger_Vehicle_Licenses_table` GROUP BY `ZipCode` ORDER BY COUNT(*) DESC LIMIT 1; "
    E = cursor.execute(sql20).fetchone()[0]
    print(E)

def main():
    create_db_and_table()
    add__data_to_database()
    display_all_hybridfuel_base()
    print("-------")
    display_max_year()
    print("-------")
    display_vehical_models_count()
    print("-------")
    display_most_common_vehical_model()
    print("-------")
    display_SECOND_most_common_CITY()
    print("-------")
    display__most_common_ZIP()

main()


"""""""""
1. How large is the database in kilobytes? (You don't need to use SQL or Python for this)
    838KB
2. What percent of the cars are hybrid fuel based?
    48.65% 
3. How old is the average car (in years), based on vehicle model year?
    35 years of age
4. How many different vehicle models are there?
    197
5. What is the most common vehicle model?
    CAMRY
6  Aside from Chicago, what is the second most common city/town of origin of these cars? 
    ELMHURST
7. What zip code contains the most registered public passenger vehicles?
    60618 
"""""