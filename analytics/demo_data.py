from decimal import Decimal
from datetime import date


def portfolio_summary_demo():
    return {
        "Name": "ICICI Prudential Dividend Yield Equity Mutual Fund Direct Growth",
        "Units_bought": Decimal("9527.5830"),
        "Buy_date": date(2025, 6, 16),
        "Invest_nav": Decimal("57.7300"),
        "Amount_invested": Decimal("550000.0000"),
        "Latest_NAV": Decimal("60.5800"),
        "Latest_NAV_date": date(2026, 7, 30),
        "latest_value": Decimal("577180.9781"),
        "Profit and loss": Decimal("27180.9781"),
        "Absolute Return": "4.94%",
        "CAGR": "4.40%",
        "XIRR": None
    }