import os

from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}



#DB_CONFIG = {
    #"host": "localhost",
    #"user": "root",
    #"password": "deva02",
    #"database": "mutual_fund_dashboard"
#}