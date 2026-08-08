from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
'''----------------------------------------------------------------------------------'''

import streamlit as st
from analytics.curate_data import portfolio_summary
from analytics.get_data import nav_history
import pandas as pd
import altair as alt

portfolio = portfolio_summary("ICICI Prudential Dividend Yield Equity Mutual Fund Direct Growth")
st.title("Mutual Fund Dashboard")
st.subheader(portfolio["Name"])

invest_column, current_column = st.columns(2)


def money(value):
    return f"₹{value:,.2f}"


with invest_column:
    st.metric(
        label="Invested Value",
        value=money(portfolio['Amount_invested'])
    )
with current_column:
    st.metric(
        label="Curent Market Value",
        value=money(portfolio['latest_value'])
    )

profitLossColumn, absoluteReturn = st.columns(2)

with profitLossColumn:
    st.metric(
        label="Profit/loss",
        value=money(portfolio['Profit and loss'])
    )
with absoluteReturn:
    st.metric(
        label="Absolute Return",
        value=f"{portfolio['Absolute Return']}"
    )

latestNAV, latestNAVDate = st.columns(2)

with latestNAV:
    st.metric(
        label="Latest nav",
        value=money(portfolio['Latest_NAV'])
    )
with latestNAVDate:
    st.metric(
        label="NAV as of:",
        value=f"{portfolio['Latest_NAV_date']}"
    )
# --------------------------------Line Chart Creation-------------------------------------------
history = nav_history()
df = pd.DataFrame(
    history,
    columns=["Date", "NAV"]
)
df["NAV"] = df["NAV"].astype(float)
min_nav = float(df["NAV"].min()) - 10
max_nav = float(df["NAV"].max()) + 10

Plot = (
    alt.Chart(df)
    .mark_line()
    .encode(
        x="Date:T",
        y = alt.Y(
            "NAV:Q",
            scale=alt.Scale(
                domain=[min_nav,max_nav]
            )
        )
    )
)

charts = st.container()
with charts:
    st.subheader("NAV Trend")
    st.altair_chart(Plot,use_container_width=True)
