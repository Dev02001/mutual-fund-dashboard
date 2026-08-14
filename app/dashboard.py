
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
'''----------------------------------------------------------------------------------'''

import streamlit as st
from analytics.curate_data import (
    portfolio_summary, portfolio_value_history,
    days,
    annualised_std, beta, benchmark_cagr, alpha)

from analytics.get_data import nav_history
import pandas as pd
import altair as alt

# --------------------Reusable Function section---------------------------------


@st.cache_data
def money(value):
    return f"₹{value:,.2f}"

# --------------------------------KPI Section start-------------------------------


portfolio = portfolio_summary("ICICI Prudential Dividend Yield Equity Mutual Fund Direct Growth")
st.title("Mutual Fund Dashboard")
st.subheader(portfolio["Name"])

# ------------------------------Tab Creations-------------------------------------

KPI_tab, Trend_tab, Risk_ratio_tab = st.tabs(["KPI", "Trend", "Risk Ratios"])

# --------------------------------KPI Section Row 1-------------------------------------------------
with KPI_tab:
    invest_column, current_column = st.columns(2)

    with invest_column:
        st.metric(
            label="Invested Value",
            value=money(portfolio['Amount_invested']),
        )
    with current_column:
        st.metric(
            label="Current Market Value",
            value=money(portfolio['latest_value'])
        )
# --------------------------------KPI Section Row 2-------------------------------------------------
with KPI_tab:
    profitLossColumn, absoluteReturn = st.columns(2)
    with profitLossColumn:
        st.metric(
            label="Profit/loss",
            value=money(portfolio['Profit and loss']),
        )
    with absoluteReturn:

        st.metric(
            label="Absolute Return",
            value=f"{portfolio['Absolute Return']}"
        )

# --------------------------------KPI Section Row 3-------------------------------------------------
with KPI_tab:
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

# ---------------------------------Returns Container------------------------------------------------------------
with KPI_tab:
    annualised_return = portfolio["CAGR"]
    return_container = st.container(border=True)
    with return_container:
        cagr_column, xirr_column = st.columns(2)
        with cagr_column:
            st.metric(
                label="CAGR",
                value=f"{annualised_return:.2%}"
            )
        with xirr_column:
            st.metric(
                label="XIRR",
                value=portfolio['Absolute Return']
            )
# --------------------------------Line Chart Creation for nav history-------------------------------------------

with Trend_tab:
    history_of_nav = nav_history()
    nav_table = pd.DataFrame(
        history_of_nav,
        columns=["Date", "NAV"]
    )
    nav_table["NAV"] = nav_table["NAV"].astype(float)
    min_nav = float(nav_table["NAV"].min()) - 10
    max_nav = float(nav_table["NAV"].max()) + 10
    Plot = (
        alt.Chart(nav_table)
        .mark_line()
        .encode(
            x="Date:T",
            y=alt.Y(
                "NAV:Q",
                scale=alt.Scale(domain=[min_nav, max_nav])
            )
        )
    )
    charts = st.container()
    with charts:
        st.subheader("NAV Trend")
        st.altair_chart(Plot, use_container_width=True)

# ----------------------------------------Portfolio value over-time Line-chart-----------------------------------
with Trend_tab:
    amount_overtime = portfolio_value_history(portfolio["Units_bought"])

    min_nav = float(amount_overtime["Amount"].min()) - 10000
    max_nav = float(amount_overtime["Amount"].max()) + 10000

    Plot = (
        alt.Chart(amount_overtime)
        .mark_line()
        .encode(
            x="Date:T",
            y=alt.Y(
                "Amount:Q",
                scale=alt.Scale(
                    domain=[min_nav, max_nav]
                )
            )
        )
    )

    Portfolio_amount_chart = st.container()
    with Portfolio_amount_chart:
        st.subheader("Amount Trend")
        st.altair_chart(Plot, use_container_width=True)

# ----------------------------------------------Risk Ratio section-----------------------------------
with Risk_ratio_tab:
    st.subheader(f"Risk metrics based on {days()} daily return observations")
    ratio = st.container(border=True)
    with ratio:
        standard_deviation_block, beta_block = st.columns(2)
        with standard_deviation_block:
            std = annualised_std()
            st.metric(
                label="Annualised Volatility",
                value=f"{std:.2%}",
                delta_description=f"Volatility based on {days()} daily return observations"
            )
        with beta_block:
            beta_value = beta()
            st.metric(
                label="Beta",
                value=f"{beta_value:.2}",
                delta_description="BenchMark is Nifty 50"
            )
        alpha_ratio, Benchmark_return = st.columns(2)
        with alpha_ratio:
            alpha_value = alpha()
            st.metric(
                label="Alpha",
                value=f"{alpha_value:.2}",
                delta_description="Risk-free-rate is 6%"
            )
        with Benchmark_return:
            benchmark_return_value = benchmark_cagr()
            st.metric(
                label="Benchmark Return",
                value=f"{benchmark_return_value:.2%}"
            )
