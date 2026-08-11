import mysql.connector
import pandas as pd
from config.db_config import DB_CONFIG

# -------------------------SQL Queries--------------------------
create_index_table = '''
    create table index_history (
        index_date Date primary key NOT NULL,
        index_value decimal(10,4),
        scrape_timestamp timestamp,
        create_at timestamp
    )
'''

query_to_insert = '''
    insert into index_history(
        index_date,
        index_value
    )
    values (%s, %s)
    '''

check_query = '''Select * from index_history where index_date = %s'''

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

index_data = pd.read_csv("../Data_sets/NIFTY 50.csv")


def table_creation():
    connection, cursor = get_connected()
    if connection.is_connected:
        cursor.execute(create_index_table)
        connection.commit()
        disconnect(connection, cursor)
    return print("Table Created")


def check_data(data, cursor):
    cursor.execute(check_query, (data,))
    value = cursor.fetchone()
    return value is not None


def insert_data(data):
    connection, cursor = get_connected()
    data_to_insert = data[["Date", "Close"]]
    insert_count = 0
    for i in range(len(data)):

        date_value = data_to_insert["Date"].iloc[i]
        close_value = data_to_insert["Close"].iloc[i]

        data_exist = check_data(date_value, cursor)

        if data_exist is False:
            cursor.execute(query_to_insert, (date_value, close_value))
            insert_count += 1

    connection.commit()
    disconnect(connection, cursor)
    return insert_count


#print(table_creation())
print(insert_data(index_data))
