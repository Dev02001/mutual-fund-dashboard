insert_etl_log = '''insert into etl_log(
    Start_time, 
    end_time, 
    log_status, 
    records_loaded, 
    log_message
    ) 
    value(%s,%s,%s,%s,%s)'''


def log_etl_status(cursor, start_time, end_time, status, message, record_count):
    try:
        cursor.execute(insert_etl_log, (start_time, end_time, status, record_count, message))
    except Exception as e:
        print(f"There was an error {e}")
