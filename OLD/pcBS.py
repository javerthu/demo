import requests
from bs4 import BeautifulSoup
import bs4

def getText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()#状态不为200，引发异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.tbody.children:
        if isinstance(tr,bs4.element.Tag):#过滤掉tr中不是Tag类型的变量
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

def printList(ulist,num):
    tplt = '{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}'
    print(tplt.format('排名','学习名称','省份','分数',chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def main():
    unifo = []
    url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = getText(url)
    fillList(unifo,html)
    printList(unifo,20)

main()











    
