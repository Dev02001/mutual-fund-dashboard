CREATE DATABASE IF NOT EXISTS mutual_fund_dashboard
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE mutual_fund_dashboard;

DROP TABLE IF EXISTS etl_log;

CREATE TABLE etl_log (
    log_id INT NOT NULL AUTO_INCREMENT,
    Start_Time TIMESTAMP NULL,
    end_time TIMESTAMP NULL,
    log_status VARCHAR(20),
    records_loaded INT,
    log_message VARCHAR(255),
    PRIMARY KEY (log_id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS investment_transaction;

CREATE TABLE investment_transaction (
    transaction_id INT NOT NULL AUTO_INCREMENT,
    fund_name VARCHAR(255) NOT NULL,
    buy_date DATE NOT NULL,
    invest_amount DECIMAL(10,4) NOT NULL,
    invest_nav DECIMAL(10,4) NOT NULL,
    bought_units DECIMAL(10,4) NOT NULL,
    PRIMARY KEY (transaction_id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS nav_history;

CREATE TABLE nav_history (
    nav_date DATE NOT NULL,
    scrape_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nav_value DECIMAL(10,4) NOT NULL,
    PRIMARY KEY (nav_date)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;