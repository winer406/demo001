import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import datetime

st.set_page_config(
    layout="wide"   #設定成 wide
)

headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

url_news1 = "https://tw.tradingview.com/markets/world-stocks/worlds-largest-companies/"
url_news2 = "https://news.cnyes.com/news/cat/wd_stock"

html_data1 = requests.get(url=url_news1,headers=headers)
html_data2 = requests.get(url=url_news2,headers=headers)
html_data2.encoding = 'utf-8'  # 確保中文顯示正常

news1 = pd.read_html(html_data1.text)
soup = BeautifulSoup(html_data2.text, 'html.parser')

st.markdown("## 全球市值前20大公司")
st.dataframe(news1[0].head(20), use_container_width=True)

st.markdown("## 股價")
stock_list = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'META', 'TSM']
for ticker in stock_list:
    try:

        # 取得即時價格
        todays_data = yf.download(tickers=ticker,period="2d")  # 最近兩天
        current_price = todays_data["Close"].iloc[-1].item()
        prev_close = todays_data["Close"].iloc[-2].item()

        # 計算漲跌幅
        change = current_price - prev_close
        pct_change = (change / prev_close) * 100

        # 判斷顏色
        color = "green" if change > 0 else "red"

        # 顯示股價 + 漲跌幅
        st.markdown(
            f"""
            <h>
                {ticker} 最新股價: {current_price:.2f} USD
                <span style="color:{color}">({change:+.2f}, {pct_change:+.2f}%)</span>
            </h>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"取得股價資料失敗: {e}")

st.markdown("## 即時財經新聞")
titles =soup.find_all('p',class_='list-title t2a6dmk')
for title in titles:
    link = title.find('a')['href']
    url = "https://news.cnyes.com" + link
    text = title.text.strip()
    st.markdown(f"[{text}]({url})")

