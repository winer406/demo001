import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

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
<<<<<<< HEAD
#st.write(news[0].head(10))
st.dataframe(news1[0].head(10), use_container_width=True)
=======
st.dataframe(news1[0].head(20), use_container_width=True)
>>>>>>> 8ad23c21089746b8bcd959235768183adb0dba59

st.markdown("## 即時財經新聞")
titles =soup.find_all('p',class_='list-title t2a6dmk')
for title in titles:
    link = title.find('a')['href']
    url = "https://news.cnyes.com" + link
    text = title.text.strip()

<<<<<<< HEAD
    st.markdown(f"[{text}]({url})")
=======
    st.markdown(f"[{text}]({url})")




>>>>>>> 8ad23c21089746b8bcd959235768183adb0dba59
