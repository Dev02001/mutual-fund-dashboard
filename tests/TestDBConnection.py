import mysql.connector
from config.db_config import DB_CONFIG

connection = mysql.connector.connect(**DB_CONFIG)

if connection.is_connected():
    print("Connected")
    connection.close()
else:
    print("Not connected")
