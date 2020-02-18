# dailyfresh
B2C(Business-to-Customer), 企业对个人的一种商业模式，简称"商对客". 商对客是电子商务的一种模式，这种电子商务一般以网络零售业为主，主要借助于互联网开展在线销售活动。 B2C即企业通过互联网为消费者提供一个新型的购物环境——网上商店，消费者通过网络在网上购物、网上支付等消费行为。


#### 技术栈
- 语言：Python3.* (Django)
- 数据库: MySql、 redis
- 任务队列(异步处理): celery(django-celery)
- 搜索引擎(商品检索)：  haystack(django-haystack)、whoosh、二次开发
- web服务器配置: Nginx+ uwsgi(阿里云服务器)
- 开发环境： PyCharm、Cenos7、Visual Studio Code


#### 技术架构
* 开发架构
采用BS结构, 即Browser/Server(浏览器/服务器)结构,构建一个web的网站商城系统, 其架构逻辑:
![frame](Readme/framework.png)


### Links
* 项目地址
[http://47.75.166.141/](http://47.75.166.141/)
* Nginx
[https://nginx.org/download/](https://nginx.org/download/)
* 支付宝api
[https://open.alipay.com/platform/home.htm](https://open.alipay.com/platform/home.htm)
* celery
[http://docs.jinkan.org/docs/celery/](http://docs.jinkan.org/docs/celery/)

