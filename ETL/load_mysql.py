import mysql.connector
from config.db_config import DB_CONFIG


connection = None
cursor = None

def get_connected ():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Connected successfully to MySQL !")
            cursor=connection.cursor()
            return connection, cursor
    except mysql.connector.Error as e:
        print("Connection Unsuccessfull", e)
        return None

def connection_close(connection,cursor):
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
        print("Connection closed")


'''Insert into investment_transaction means load data of investment carried out'''

insert_query = ''' INSERT INTO investment_transaction (
    fund_name,
    buy_date,
    invest_amount,
    invest_nav,
    bought_units
    )
VALUES (%s, %s, %s, %s, %s) '''

insert_values = (
    "ICICI Prudential Dividend Yield Equity Mutual Fund Direct Growth",
    "2025-06-16",
    550000,
    57.73,
    9527.583
)

def investment_transaction(insert_query, insert_values):
    connection,cursor = get_connected()
    cursor.execute(insert_query,insert_values)
    connection.commit()
    connection_close(connection,cursor)

check_nav_exist = '''SELECT nav_date FROM nav_history WHERE nav_date = %s '''


def verify_nav_exist(nav_date,cursor):
    cursor.execute(check_nav_exist,(nav_date,))
    nav_exist = cursor.fetchone()
    if nav_exist is None:
        print(f"{nav_date} does not exist")
        return False
    else:
        print(f"Nav for {nav_date} Exist")
        return True

nav_insert_query = '''INSERT INTO nav_history (
    nav_value,
    nav_date
    )
    VALUES (%s, %s);'''

def insert_latest_nav(nav_value,nav_date):
    connection,cursor = get_connected()
    nav_exist = verify_nav_exist(nav_date,cursor)
    if nav_exist is False:
        cursor.execute(nav_insert_query, (nav_value,nav_date))
        print("Data inserted succesfully")
        connection.commit()
        connection_close(connection,cursor)
    else:
        print("Data already exist")
        connection_close(connection,cursor)

