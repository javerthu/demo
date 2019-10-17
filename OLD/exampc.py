import requests
def getHTML(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()#状态不为200，引发异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == '__main__':
    url = input('爬取网站:')
    print(getHTML(url))
# 一般爬虫协议http://www.baidu.com/robots.txt
