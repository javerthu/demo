import requests
from bs4 import BeautifulSoup
import bs4
import re
import random

def getText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()#状态不为200，引发异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
his = ['/item/sm/18874']
for i in range(10):
    try:
        star_url = 'https://baike.baidu.com'
        url = star_url + his[-1]
        html = getText(url)
        soup = BeautifulSoup(html,'html.parser')
        print(i,soup.find('h1').get_text(),'url:',his[-1])
        sub_urls = soup.find_all('a',{"target":"_blank",'href':re.compile('/item/(%.{2})+$')})
        if len(sub_urls) !=0:
            his.append(random.sample(sub_urls,1)[0]['href'])
        else:
            his.pop()
    except:
        print()
