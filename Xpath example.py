import requests

from lxml import etree

'''
用lxml来解析HTML代码
'''
r = requests.get('https://www.w3school.com.cn/example/xmle/books.xml')

print(type(r.content))

# 利用etree.HTML把字符串解析成HTML文档
html = etree.HTML(r.content)
print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)

# xpath的意识是，查找带有category属性值为sport的book元素
rst = html.xpath('//book[@category="web"]')
print(type(rst))
print(rst)

# xpath的意识是，查找带有category属性值为sport的book元素下的year元素
rst = html.xpath('//book[@category="web"]/price')
for i in rst:
    print(type(i))
    print(i.tag, i.text)
