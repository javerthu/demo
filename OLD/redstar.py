import requests
from bs4 import BeautifulSoup
res = requests.get("https://news.sina.com.cn/china/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
for news in soup.select('.feed-card-item'):
    print(news)
