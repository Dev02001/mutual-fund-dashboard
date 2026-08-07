import mysql.connector
from config.db_config import DB_CONFIG
from datetime import datetime
from logs.etl_log import log_etl_status

connection = None
cursor = None


def get_connected():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            return connection, cursor
    except mysql.connector.Error as e:
        print(e)
        return None, None


def connection_close(connection, cursor):
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()


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
    connection, cursor = get_connected()
    if connection is None:
        return None
    start_time = datetime.now()
    try:
        cursor.execute(insert_query, insert_values)
        end_time = datetime.now()
        record_count = cursor.rowcount
        status = "Success"
        message = "Investment Data inserted Successfully"
        log_etl_status(cursor, start_time, end_time, status, record_count, message)
        connection.commit()
    except Exception as e:
        print(e)
        if connection:
            connection.rollback()
    finally:
        connection_close(connection, cursor)


check_nav_exist = '''SELECT nav_date FROM nav_history WHERE nav_date = %s '''


def verify_nav_exist(nav_date, cursor):
    cursor.execute(check_nav_exist, (nav_date,))
    nav_exist = cursor.fetchone()
    if nav_exist is None:
        # print(f"{nav_date} does not exist")
        return False
    else:
        # print(f"Nav for {nav_date} Exist")
        return True


nav_insert_query = '''INSERT INTO nav_history (
    nav_value,
    nav_date
    )
    VALUES (%s, %s);'''


def insert_latest_nav(nav_value, nav_date):
    connection, cursor = get_connected()
    if connection is None:
        return
    nav_exist = verify_nav_exist(nav_date, cursor)
    start_time = datetime.now()
    try:
        if nav_exist is False:
            cursor.execute(nav_insert_query, (nav_value, nav_date))
            end_time = datetime.now()
            record_count = cursor.rowcount
            status = "Success"
            message = "Data inserted Successfully"
            log_etl_status(cursor, start_time, end_time, status, message, record_count)
            connection.commit()
        else:
            end_time = datetime.now()
            record_count = 0
            status = "Skipped"
            message = "Data already exists"
            log_etl_status(cursor, start_time, end_time, status, message, record_count)
            connection.commit()

    except Exception as e:
        print(e)
        if connection:
            connection.rollback()
    finally:
        connection_close(connection, cursor)
