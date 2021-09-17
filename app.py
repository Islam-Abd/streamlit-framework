#!/usr/bin/env python
# coding: utf-8

import json

import requests
from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

#stremlit
syear =pd.DataFrame(['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'],columns=['Year'])
smonth=pd.DataFrame(['January','February','March','April','May','June','July','August','September','October','November','December'],columns=['Month'])

stock = st.sidebar.text_input("Stock Ticker", 'aapl')
option1 = st.sidebar.selectbox('Select a year',syear['Year'])
option2 = st.sidebar.selectbox('Select a month',smonth['Month'])


month=option2
year=option1

filter=month+' '+year

from datetime import datetime

ticker=stock
apikey=os.getenv("apikey")

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&apikey=%s&outputsize=full'%(ticker,apikey)
r=requests.get(url)
data=r.json()



df=pd.DataFrame(data['Time Series (Daily)'])
close=df.loc['4. close',:]
close.index=pd.to_datetime(close.index,)
close=close.sort_index()

close0=pd.DataFrame(close)
close0['4. close'] = close0['4. close'].astype(float)
close0=close0.rename(columns={'4. close':'Closing Price'})
close1=close0.loc[filter]

import plotly.express as px

fig = px.line(close1, y="Closing Price", title='Stock Closing Price',labels={"index": "Date"})
st.plotly_chart(fig)


