from analytics.get_data import get_fund_details
from decimal import Decimal, ROUND_HALF_UP

# Following function will curate all the information and form a dictionary and send this curated data to dashboard.py


def portfolio_summary(name):
    fund_details = get_fund_details(name)
    total_value = current_market_value(fund_details["units_bought"], fund_details["latest_nav"])
    portfolio_detail = {
        "Name": fund_details["fund_name"],
        "Units_bought": fund_details["units_bought"],
        "Buy_date" : fund_details["buying_date"],
        "Invest_nav" : fund_details["buying_nav"],
        "Amount_invested": fund_details["invest_amount"],
        "Latest_NAV": fund_details["latest_nav"],
        "Latest_NAV_date": fund_details["latest_nav_date"],
        "latest_value": total_value,
        "Profit and loss": profit_loss(total_value, fund_details["invest_amount"]),
        "XIRR": xirr(),
        "Absolute Return": absolute_return(total_value,fund_details["invest_amount"]),
        "CAGR": cagr(total_value,fund_details["invest_amount"],fund_details["buying_date"],fund_details["latest_nav_date"])
    }
    return portfolio_detail


def current_market_value(units_owned, current_nav):
    latest_value = current_nav*units_owned
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
    Absolute_return = (market_value - invest_value)/invest_value
    Absolute_return = f"{Absolute_return:.2%}"
    return Absolute_return


def xirr():
    pass


def cagr(market_value, invest_value, buy_date, current_date):
    year = (current_date-buy_date).days/365.25
    CAGR = (market_value / invest_value) ** (Decimal(1)/Decimal(year)) - 1
    CAGR = f"{CAGR:.2%}"
    return CAGR


#fund = portfolio_summary("ICICI Prudential Dividend Yield Equity Mutual Fund Direct Growth")
#pprint(fund, indent=4)
#print(fund['latest_value'])
