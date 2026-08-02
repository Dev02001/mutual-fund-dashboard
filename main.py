from ETL.scraper import fetch_funds_data
from ETL.scraper import get_fund_by_scheme_code
from ETL.scraper import get_latest_nav
from ETL.validator import validate_nav_data
from ETL.load_mysql import insert_latest_nav
import json

#Extract all the funds from the icic website
data = fetch_funds_data()

#extract only ICICI dividened fund
fund_name = get_fund_by_scheme_code(data,"8573")

#extract nav and date from extracted ICICI dividened fund
latest_nav, nav_date = get_latest_nav(fund_name)

#Formats the nav and date into relevant data format
formatted_nav, formated_nav_date = validate_nav_data( latest_nav, nav_date)

#Insert formated nav and date into nav_history table in database
insert_latest_nav(formatted_nav,formated_nav_date)