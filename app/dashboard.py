import os
import sys
import streamlit as st

st.write("Current working directory:", os.getcwd())
st.write("Python path:", sys.path)
st.title("Testing")

#from analytics.curate_data import portfolio_summary
#from analytics.demo_data import portfolio_summary_demo


#portfolio = portfolio_summary("ICICI Prudential Dividend Yield Equity Mutual Fund Direct Growth")
#portfolio = portfolio_summary_demo()
#st.title("Mutual Fund Dashboard")
#st.subheader(portfolio["Name"])

#invest_column, current_column = st.columns(2)

'''def money(value):
    return f"₹{value:,.2f}"'''

#with invest_column:
    #st.metric(
        #label= "Invested Value",
        #value = money(portfolio['Amount_invested'])
    #)
#with current_column:
    #st.metric(
        #label= "Curent Market Value",
        #value= money(portfolio['latest_value'])
    #)

#profitLossColumn, absoluteReturn = st.columns(2)

#with profitLossColumn:
    #st.metric(
        #label="Profit/loss",
        #value = money(portfolio['Profit and loss'])
    #)
#with absoluteReturn:
    #st.metric(
        #label= "Absolute Return",
        #value=f"{portfolio['Absolute Return']}"
    #)

'''latestNAV, latestNAVDate = st.columns(2)

with latestNAV:
    st.metric(
        label= "Latest nav",
        value=money(portfolio['Latest_NAV'])
    )
with latestNAVDate:
    st.metric(
        label="NAV as of:",
        value=f"{portfolio['Latest_NAV_date']}"
    )'''
