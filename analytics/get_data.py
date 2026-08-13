import pandas as pd

from ETL.load_mysql import (get_connected, connection_close)


class Queries:
    fund_detail = '''Select fund_name, sum(invest_amount), sum(bought_units),avg(invest_nav) from investment_transaction where 
    fund_name = %s '''
    invest_date = '''select buy_date from investment_transaction where fund_name = %s '''

    # Following query retrieves the latest NAV value from the nav_history table
    nav_value_query = '''SELECT nav_value, nav_date FROM nav_history ORDER BY nav_date DESC limit 1'''

    # Following query reteieves nav history
    nav_history_query = '''select nav_date, nav_value from nav_history order by nav_date DESC'''

    # Follwoing query retrieves index history
    index_history_query = '''Select index_date, index_value from index_history order by index_date DESC'''


class DbConnection:
    def __init__(self):
        self.connection, self.cursor = get_connected()

    def close(self):
        connection_close(self.connection, self.cursor)


query = Queries()


def get_fund_details(name):
    database_connection = DbConnection()
    try:
        investment = get_investment_detail(name, database_connection.cursor)
        fund_nav = latest_nav_value(database_connection.cursor)
        investment_details = (*investment, *fund_nav)
        keys = ["fund_name", "invest_amount", "units_bought", "buying_nav", "buying_date", "latest_nav",
                "latest_nav_date"]
        investment_details = dict(zip(keys, investment_details))
        return investment_details
    finally:
        database_connection.close()


def get_investment_detail(name, db_cursor):
    n = (name,)
    db_cursor.execute(query.fund_detail, n)
    detail = db_cursor.fetchone()
    db_cursor.execute(query.invest_date, n)
    invest_date = db_cursor.fetchone()
    Fund_data = (*detail, *invest_date)
    if Fund_data is not None:
        return Fund_data
    else:
        return None


# Following Functions Returns the Latest NAV


def latest_nav_value(db_cursor):
    db_cursor.execute(query.nav_value_query)
    value = db_cursor.fetchone()
    if value:
        nav_value, nav_date = value
        return nav_value, nav_date
    else:
        print("Data was not retrieved")
        return None


# Following function returns entire table containing nav history
def get_nav_history(cursor):
    cursor.execute(query.nav_history_query)
    return cursor.fetchall()


def nav_history():
    connection = DbConnection()
    try:
        return get_nav_history(connection.cursor)
    finally:
        connection.close()


def get_index_history():
    connection, cursor = get_connected()
    cursor.execute(query.index_history_query)
    index_history = cursor.fetchall()
    if index_history is not None:
        return index_history
    else:
        return None