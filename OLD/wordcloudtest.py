import wordcloud  #不能创建wordcloud.py文件不然会报错
import jieba
import imageio
mask=imageio.imread('E:/python/file/fivestart.png')
f=open('E:/python/file/cybg.txt','r',encoding='utf-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)
c=wordcloud.WordCloud(font_path='msyh.ttc',width=1000,height=700,\
                      background_color='white',max_words=30,mask=mask)
c.generate(txt)
c.to_file('E:/python/file/cybg.png')
