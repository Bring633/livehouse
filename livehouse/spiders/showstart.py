# -*- coding: utf-8 -*-
import scrapy
import json
from livehouse.items import LivehouseItem
import livehouse.settings as settings
import time
import random

class ShowstartSpider(scrapy.Spider):
    name = 'showstart'
    allowed_domains = ['https://www.showstart.com/','https://www.damai.cn/']
    start_urls = []

    def __init__(self,category=None,start_date=None,end_date = None,loc=None,shower=None):

        self.category = category
        self.start_date = start_date
        self.end_date = end_date
        self.loc = loc
        self.shower = shower
        
        return
    
    def start_requests(self):
        
        location_code = settings.showstart_location_code_dict[self.loc]
        showstart_live_type_code = settings.showstart_live_type_code
        
        showstart_url = \
            'https://www.showstart.com/event/list?pageNo=1&pageSize=20&cityCode={0}&keyword={1}&showStyle={2}&timeRange={start}_{end}'\
                .format(location_code,self.keyword,start=self.start_date,end=self.end_date)
            
        for i in range(len(showstart_live_type_code)):
            url = showstart_url.format(showstart_live_type_code[i],self.start_date,self.end_date)
            time.sleep(0.1+random.random())
            yield scrapy.Request(url,self.parse_showstart,meta = {'url':showstart_url})
        
        return None

    def parse_showstart(self, response):
        
        data = json.loads(response.text)
        showstart_url = response.meta['url']
        
        show_urls = response.xpath("//div[@class=\"list-box clearfix\"]/a/@href")
        page = response.xpath('//ul[@class = "el-pager"]/li/text()').extract()[-1]
        
        for i in range(page):
            url = page.format(i)
            time.sleep(0.1+random.random())
            yield scrapy.Request(url,self.parse_showstart)
            
        for i in show_urls:
            time.sleep(0.1+random.random())
            yield scrapy.Request(i,self.show_start_content_extract)
            
        return None
            
    def show_start_content_extract(self,response):
        
        item = LivehouseItem()
        
        item['category'] = ','.join(response.xpath('//div[@class="label"]/label/text()').extract())
        item['']
        """       
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    loc = scrapy.Field()#所在城市
    name = scrapy.Field()#场次的名字
    shower = scrapy.Field()#乐队
    state = scrapy.Field()#售票状态
    provider = scrapy.Field()#哪里售卖
    web = scrapy.Field()#网址
    sale_price = scrapy.Field()#价格
"""
        
        return 
        
        
        
        
        
        
        
        