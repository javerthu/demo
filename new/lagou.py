import requests
import json
from  pymongo import *
import time
#获得客户端，建立链接
clien = MongoClient('mongodb://localhost:27017')
db = clien['51job']#调用51job数据库
stu = db.lagou #lagou collection


def update():
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get(
        'https://www.lagou.com/jobs/list_Python?isSchoolJob=1',
        headers=headers)  # 请求原网页
    r = requests.utils.dict_from_cookiejar(response.cookies)  # 获取cookies
    r["LGRID"] = r["user_trace_token"]
    r["user_trace_token"] = r["LGRID"]
    r["LGSID"] = r["LGRID"]
    r["LGUID"] = r["LGRID"]  # 构造cookies的参数
    cookies = {
        'X_MIDDLE_TOKEN': '797bc148d133274a162ba797a6875817',
        'JSESSIONID': 'ABAAABAAAIAACBI03F33A375F98E05C5108D4D742A34114',
        '_ga': 'GA1.2.1912257997.1548059451',
        '_gat': '1',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059451',
        'user_trace_token': '20190121163050-dbd72da2-1d56-11e9-8927-525400f775ce',
        'LGSID': '20190121163050-dbd72f67-1d56-11e9-8927-525400f775ce',
        'PRE_UTM': '',
        'PRE_HOST': '',
        'PRE_SITE': '',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F%3F_from_mid%3D1',
        'LGUID': '20190121163050-dbd73128-1d56-11e9-8927-525400f775ce',
        '_gid': 'GA1.2.1194828713.1548059451',
        'index_location_city': '%E5%85%A8%E5%9B%BD',
        'TG-TRACK-CODE': 'index_hotjob',
        'LGRID': '20190121163142-fb0cc9c0-1d56-11e9-8928-525400f775ce',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059503',
        'SEARCH_ID': '86ed37f5d8da417dafb53aa25cd6fbc0',
    }
    cookies.update(r)  # 更新接口的cookies
    return cookies

cookies = update()
headers = {
    'Origin': 'https://www.lagou.com',
    'X-Anit-Forge-Code': '0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/jobs/list_python?px=new&city=%E4%B8%8A%E6%B5%B7',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'X-Anit-Forge-Token': 'None',
}
params = (
    ('px', 'default'),
    ('gx', '全职'),
    ('needAddtionalResult', 'false'),
    ('isSchoolJob', '1'),
) #网页请求的params参数，也可直接?到post的url当中

data = {'first': True,
        'kd': 'python'
        }
for i in range(1, 20): #设置爬取深度参数
    print(i)
    try:
        data['pn'] = i #控制翻页
        # time.sleep(1.5) #拉钩网给定的爬取频率太低了 反正都会被被拦截，进入异常更新cookies就行了
        response = requests.post('https://www.lagou.com/jobs/positionAjax.json', headers=headers, params=params,
                                 cookies=cookies, data=data)  # 请求接口 最好找个代理ip爬取
        positon = response.json()['content']['positionResult']['result']
        c = 0
        for i in positon:
            c = c+1   #下面语句用来判断有是否重复的
            if stu.count_documents({"id": i['positionId']}) != 0:#stu.find({"id": i['positionId']}).count() != 0:
                continue
            else:
                stu.insert_one({'id':i['positionId'], 'name':i['positionName'],#stu.insert({'id':i['positionId'], 'name':i['positionName'],
                            'addr':str(i['city'])+str(i['district']),
                            'savage':i['salary'], 'xueli':i['education'],
                            'requr':i['positionLables'], 'posttime':i['createTime'][0:10],
                            'wky':i['workYear']})#增
                print(c, i['positionName'], str(i['city'])+str(i['district']), i['positionLables'], i['createTime'][0:10], i['salary'], i['education'], i['workYear'])
                print(i['positionId'])
    except:
        cookies = update()
        data['pn'] = i #控制翻页
        time.sleep(1.5)
        response = requests.post('https://www.lagou.com/jobs/positionAjax.json', headers=headers, params=params,
                                 cookies=cookies, data=data, proxies=proxies)  # 请求接口
        positon = response.json()['content']['positionResult']['result']
        c = 0
        for i in positon:
            c = c+1   #下面语句用来判断有是否重复的
            if stu.count_documents({"id": i['positionId']}) != 0:#stu.find({"id": i['positionId']}).count() != 0:
                continue
            else:
                stu.insert_one({'id':i['positionId'], 'name':i['positionName'],#stu.insert({'id':i['positionId'], 'name':i['positionName'],
                            'addr':str(i['city'])+str(i['district']),
                            'savage':i['salary'], 'xueli':i['education'],
                            'requr':i['positionLables'], 'posttime':i['createTime'][0:10],
                            'wky':i['workYear']})#增
                print(c, i['positionName'], str(i['city'])+str(i['district']), i['positionLables'], i['createTime'][0:10], i['salary'], i['education'], i['workYear'])
                print(i['positionId'])
