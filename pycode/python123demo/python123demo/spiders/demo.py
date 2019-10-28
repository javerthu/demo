# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from python123demo.items import DemoItem
import re


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['https://www.51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?workyear=01',
                 # 'https://search.51job.com/list/000000,000000,0000,00,9,99,jave,2,1.html',
                  ]
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }

    def parse(self, response):
        rst = response.xpath("//div/p/span/a/@href") #response.xpath("//a/@href").re("https://.*html.*")
        for i in rst:
            url = i.extract()
            yield scrapy.Request(url, callback=self.parse_deal)

    def parse_deal(self, response):
        savege = self.savege(response)
        compy = self.compy(response)
        job = self.job(response)
        yq = self.yq(response)
        print(savege, job, yq)
        item = DemoItem(id=response.url, savege=savege, compy=compy, job=job, yq=yq)
        yield item

        # Continue crawling
        urls = response.xpath("//div[@class='e']/a[@class='name']/@href").re('https://jobs.51job.com.*html.*')
        for url in urls:
            url = url
            yield scrapy.Request(url, callback=self.parse_deal)


    def savege(self, response):
        savege = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong')#可以在strong后加/text()
        for i in savege:
            try:
                savege = i.extract().strip('</strong>')
                return savege
            except:
                return ''

    def compy(self, response):
        compy = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]/text()')
        for i in compy:
            try:
                compy = i.extract()
                return compy
            except:
                return ''

    def job(self, response):
        job = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()')
        for i in job:
            try:
                job = i.extract()
                return job
            except:
                return ''

    def yq(self, response):
        rst = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[2]|'
                             +'/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[3]|'
                             +'/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[4]|'
                             +'/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[5]')
        yq = ''
        for i in rst:
            try:
                yq = yq + ' ' + str(i.extract())
            except:
                yq = yq + ''
        return yq


# import requests
# from bs4 import BeautifulSoup
# import re
# def getText(url):
#     try:
#         kv = {'user-agent':'Mozilla/5.0'}
#         r = requests.get(url,headers=kv,timeout=30)
#         r.raise_for_status()#状态不为200，引发异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ''
# url = "https://www.51job.com/"
# soup = BeautifulSoup(getText(url),'html.parser')
# link = soup('a', href = re.compile(r"https://.*html.*"))
# for i in link:
#     print(i['href'])