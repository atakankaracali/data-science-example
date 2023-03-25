import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
# Sipmle Stock Price App
----------------------------------------
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
-----------------------------------------
Shown are the stock **closing price** and ***volume*** of Google!

"""
)
# st.write içinde # sayısı arttıkça h elementi küçülür.
# st.write içinde ** arasına yazılan kalın, *** arasına yazılan italic olur.
tickerSymbol = "TSLA"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period="ld", start="2010-5-31", end="2023-2-20")

st.write(
    """
## Closing Price
"""
)
st.line_chart(tickerDf.Close)
st.write(
    """
## Volume Price
"""
)
st.line_chart(tickerDf.Volume)
