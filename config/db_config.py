from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
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