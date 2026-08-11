import mysql.connector
import pandas as pd
from config.db_config import DB_CONFIG

# -------------------------------Local Database connection---------------
'''db_config = {
    "user": "root",
    "port": "3306",
    "password": "deva02",
    "database": "mutual_fund_dashboard",
    "host": "localhost"
}'''

# -------------------------SQL Queries--------------------------

query_to_insert = '''
    insert into nav_history(
        nav_date,
        nav_value
    )
    values (%s, %s)
    '''

check_query = '''Select * from nav_history where nav_date = %s'''

# ---------------------------------Database connection-----------------------------------


def get_connected():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            print("Connected successfully.")
            return connection, cursor
    except Exception as e:
        print("Error:", e)
        return None, None


def disconnect(connection, cursor):
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Disconnected")
        return


# -----------------------------Execution Part---------------------------

nav_data = pd.read_csv("nav_history.csv")


def check_data(data, cursor):
    cursor.execute(check_query, (data,))
    value = cursor.fetchone()
    return value is not None


def insert_data(data):
    connection, cursor = get_connected()
    insert_count = 0
    for i in range(len(data)):

        date_value = data["Date"].iloc[i]
        NAV_value = data["NAV"].iloc[i]

        data_exist = check_data(date_value, cursor)

        if data_exist is False:
            cursor.execute(query_to_insert, (date_value, NAV_value))
            insert_count += 1

    connection.commit()
    disconnect(connection, cursor)
    return insert_count


#print(table_creation())
print(insert_data(nav_data))

#print(nav_data)
