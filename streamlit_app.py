import streamlit as st
import pandas as pd
import requests

headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

url = "https://tw.tradingview.com/markets/world-stocks/worlds-largest-companies/"

html_data = requests.get(url=url,headers=headers)
news = pd.read_html(html_data.text)

st.title("My News")
st.dataframe(news[0], use_container_width=True)



