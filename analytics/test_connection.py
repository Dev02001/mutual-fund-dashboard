import mysql.connector
from config.db_config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)

print("Connected!")

conn.close()