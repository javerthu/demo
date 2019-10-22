import requests

from lxml import etree

'''
用lxml来解析HTML代码
'''
def getText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()#状态不为200，引发异常
        r.encoding = r.apparent_encoding
        return r
    except:
        return ''
c = 0
s = input('输入想查询的职位:')
star_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html'
for i in range(1, eval(input('爬取深度:'))+1):
    url = star_url.format(s, i)
    r = getText(url)

    print(type(r.content))
    # 利用etree.HTML把字符串解析成HTML文档
    html = etree.HTML(r.content)
    print(type(html))
    rst = html.xpath("//div/p/span/a")
    for i in rst:
        c = c + 1
        print(c, i.xpath("@href")[0], i.text.replace(' ', ''))