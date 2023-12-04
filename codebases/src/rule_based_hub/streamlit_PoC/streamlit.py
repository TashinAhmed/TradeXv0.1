import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import yfinance as yf # https://pypi.org/project/yfinance/
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

import datetime

import base64
from io import BytesIO


#############################################################################################################################
# sidebar with select box + datetime format along with calendar
#############################################################################################################################

option = st.sidebar.selectbox('Select one symbol', ( 'AAPL', 'MSFT',"SPY",'WMT'))

today = datetime.date.today()
before = today - datetime.timedelta(days=700)

start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)

if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')




#############################################################################################################################
# stock data 
#############################################################################################################################


# download data
df = yf.download(option, start=start_date, end=end_date, progress=False)

# Bollinger bands
indicator_bb = BollingerBands(df['Close'])

bb = df
bb['bb_h'] = indicator_bb.bollinger_hband()
bb['bb_l'] = indicator_bb.bollinger_lband()
bb = bb[['Close', 'bb_h', 'bb_l']]

# MACD (Moving Avg Convergence Divergence)
macd = MACD(df['Close']).macd()

# RSI (Relative Strength Index)
rsi = RSIIndicator(df['Close']).rsi()


#############################################################################################################################
# setting up the application
#############################################################################################################################

# plot the price and the BB bands
st.write("Stock BB Bands")
st.line_chart(bb)

progress_bar = st.progress(0)

# plot MACD
st.write("Stock MACD")
st.area_chart(macd)

# plot RSI
st.write("Stock RSI")
st.line_chart(rsi)

# data of recent days
st.write("Recent data")
st.dataframe(df.tail(10))




def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()

    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="download.xlsx">Download excel file</a>'

st.markdown(get_table_download_link(df), unsafe_allow_html=True)