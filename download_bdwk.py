import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Baiduspider-image'} #用Mozilla/5.0访问呢的txt文件是乱码 很郁闷
        r = requests.get(url, headers = kv, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def findPList(html):
    plist = []
    soup = BeautifulSoup(html, "html.parser")
    plist.append(soup.title.string)
    for div in soup.find_all('div', attrs={"class": "bd doc-reader"}):
        plist.extend(div.get_text().split('\n'))

    plist = [c.replace(' ', '') for c in plist]
    plist = [c.replace('\x0c', '') for c in plist]
    return plist

def printPList(plist, path = 'baiduwenku.txt'):
    file = open(path, 'w')
    for str in plist:
        file.write(str)
        file.write('\n')
    file.close()

def main():
    url = 'https://wenku.baidu.com/view/d3056e1be97101f69e3143323968011ca300f70c.html'
    html = getHTMLText(url)
    plist = findPList(html)
    printPList(plist)

main()