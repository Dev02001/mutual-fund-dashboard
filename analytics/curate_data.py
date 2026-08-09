import numpy as np
import pandas as pd
from analytics.get_data import get_fund_details, nav_history
from decimal import Decimal, ROUND_HALF_UP


# Following function will curate all the information and form a dictionary and send this curated data to dashboard.py


def portfolio_summary(name):
    fund_details = get_fund_details(name)
    total_value = current_market_value(fund_details["units_bought"], fund_details["latest_nav"])
    portfolio_detail = {
        "Name": fund_details["fund_name"],
        "Units_bought": fund_details["units_bought"],
        "Buy_date": fund_details["buying_date"],
        "Invest_nav": fund_details["buying_nav"],
        "Amount_invested": fund_details["invest_amount"],
        "Latest_NAV": fund_details["latest_nav"],
        "Latest_NAV_date": fund_details["latest_nav_date"],
        "latest_value": total_value,
        "Profit and loss": profit_loss(total_value, fund_details["invest_amount"]),
        "XIRR": xirr(),
        "Absolute Return": absolute_return(total_value, fund_details["invest_amount"]),
        "CAGR": cagr(total_value, fund_details["invest_amount"], fund_details["buying_date"],
                     fund_details["latest_nav_date"])
    }
    return portfolio_detail


def current_market_value(units_owned, current_nav):
    latest_value = current_nav * units_owned
    rounded_value = latest_value.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    return rounded_value


def profit_loss(current_value, total_invested):
    value = current_value - total_invested
    if value > 0:
        return value
    elif value == 0:
        return value
    else:
        return value


def absolute_return(market_value, invest_value):
    absolute_return = (market_value - invest_value) / invest_value
    absolute_return = f"{absolute_return:.2%}"
    return absolute_return


def xirr():
    pass


def cagr(market_value, invest_value, buy_date, current_date):
    year = (current_date - buy_date).days / 365.25
    CAGR = (market_value / invest_value) ** (Decimal(1) / Decimal(year)) - 1
    CAGR = f"{CAGR:.2%}"
    return CAGR


def portfolio_value_history(units):
    portfolio_history = []
    history = nav_history()
    for date, nav in history:
        portfolio_value = nav * units
        portfolio_history.append((date, portfolio_value))
    value_over_time = pd.DataFrame(
        portfolio_history,
        columns=["Date", "Amount"],
    )
    value_over_time["Amount"] = value_over_time["Amount"].astype(float)
    return value_over_time

def daily_nav_return():
    nav_return = []
    nav_data = nav_history()
    nav_df = pd.DataFrame(
        nav_data,
        columns=["Date", "NAV"]
    )
    nav_df["Date"] = pd.to_datetime(nav_df["Date"])
    for i in range(1, len(nav_df)):

        date_gap = (
            nav_df["Date"].iloc[i]
            - nav_df["Date"].iloc[i - 1]
        ).days

        if date_gap <= 4:

            daily_return = float(
                (
                    nav_df["NAV"].iloc[i]
                    - nav_df["NAV"].iloc[i - 1]
                )
                / nav_df["NAV"].iloc[i - 1]
            )

            nav_return.append(
                (nav_df["Date"].iloc[i], daily_return)
            )

    daily_return_df = pd.DataFrame(
        nav_return,
        columns=["Date", "Daily_Return"]
    )

    return daily_return_df

def standard_deviation():
    daily_return = daily_nav_return()
    return daily_return["Daily_Return"].std()
def annualised_std():
    std = standard_deviation()
    annualised = std * np.sqrt(252)
    return annualised

def days ():
    no_day = daily_nav_return()
    day_count = no_day.shape[0]
    return day_count




