import re
import requests

def gettext(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()#状态不为200，引发异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def page(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])#获得键值对后面部分
            name = eval(tlt[i].split(':')[1])
            ilt = ilt.append([price,name])
    except:
        return ""

def printGoods(ilt):
    tplt = '{0:4}\t{1:8}\t{2:16}'
    print(tplt.format('序号','价格','商品名称'))
    count = 0
    for g in ilt :
        print(tplt.format(count,g[0],g[1]))


def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    ilt = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = gettext(url)
            page(ilt,html)
        except:
            continue
    printGoods(ilt)

main()
