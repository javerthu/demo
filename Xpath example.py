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
url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
r = getText(url)

print(type(r.content))
# 利用etree.HTML把字符串解析成HTML文档
html = etree.HTML(r.content)
print(type(html))
rst = html.xpath("//div/p/span/a")
for i in rst:
    print(i.xpath("@href")[0], i.text.replace(' ', ''))