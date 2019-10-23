import requests
import os
url = 'http://image.ngchina.com.cn/2019/1023/20191023042117108.jpg'
root = 'E://python//pic//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not  os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')