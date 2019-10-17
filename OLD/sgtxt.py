import jieba
import requests
url = 'https://python123.io/resources/pye/threekingdoms.txt'
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv,timeout=30)
    r.raise_for_status()#状态不为200，引发异常
    r.encoding = r.apparent_encoding
except:
    print( '产生异常')
f = open('E:/python/file/kingdom.txt','w+',encoding='utf-8') 
f.write(r.text)
f.close()


txt = open('E:/python/file/kingdom.txt','r',encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(5):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))

