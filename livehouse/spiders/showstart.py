# -*- coding: utf-8 -*-
import scrapy
import json
from livehouse.items import LivehouseItem
import livehouse.settings as settings
import time
import random
import logging
import re


class ShowstartSpider(scrapy.Spider):
    name = 'showstart'
    allowed_domains = ['showstart.com','damai.cn']
    start_urls = ['https://www.showstart.com']

    def __init__(self,category='',start_date='',end_date = '',loc='',shower=''):

        self.category = category
        self.start_date = start_date
        self.end_date = end_date
        self.loc = loc
        self.shower = shower
        self.target_shower = shower
        
        return None
    
    def start_requests(self):
        
        location_code = settings.showstart_location_code_dict[self.loc]
        showstart_live_type_code = settings.showstart_live_type_code
        
        showstart_url = \
            'https://www.showstart.com/event/list?pageNo=1&pageSize=20&cityCode={0}&keyword={1}&showStyle={2}&timeRange={start}_{end}'\
                .format(location_code,self.shower,'{0}',start=self.start_date,end=self.end_date)
        
        for i in range(len(showstart_live_type_code)):
            url = showstart_url.format(showstart_live_type_code[i])
            time.sleep(0.1+random.random())
            yield scrapy.Request(url,self.parse_showstart,meta = {'url':showstart_url},dont_filter= True)
        
        return None

    def parse_showstart(self, response):
        
        if response.text == None:
            return None
        showstart_url = response.meta['url']
        item_url = "https://www.showstart.com"
        
        show_urls = response.xpath("//div[@class=\"list-box clearfix\"]/a/@href").extract()
        page = response.xpath('//ul[@class = "el-pager"]/li/text()').extract()
        
        show_date = response.xpath("//div[@class='time']/text()").extract()
        
        if len(page) != 0:
            page = int(page[-1])
        else:
            return None
        
        for i in range(page):
            url = showstart_url.format(i)
            time.sleep(0.1+random.random())
            yield scrapy.Request(url,self.page_showstart,dont_filter= True,meta = {'url':showstart_url},)
            
        for i in range(len(show_urls)):
            
            time.sleep(0.1+random.random())
            yield scrapy.Request(item_url+show_urls[i],self.show_start_content_extract,meta={'date':show_date[i]},dont_filter= True)
            
        return None
    
    def page_showstart(self,response):
        
        if response.text == None:
            return None
        
        show_date = response.xpath("//div[@class='time']/text()").extract()
        
        item_url = "https://www.showstart.com"
        show_urls = response.xpath("//div[@class=\"list-box clearfix\"]/a/@href").extract()

        for i in range(len(show_urls)):
            time.sleep(0.1+random.random())
            yield scrapy.Request(item_url+i,self.show_start_content_extract,meta = {'date':show_date[i]},dont_filter= True)
            
        return None
        
        
        try:
            null = response.xpath("//div[@class ='content']/h1/text()").extract()[0]
        except Exception as e:
            print(e)
            return "NOT NULL"
        return '页面不存在'
            
    def sale_state(self,response):
    
        pattern = '.*?(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*?'
        earliest = re.findall(pattern,response.text)[0]
        time_stamp = time.mktime(time.strptime(earliest , "%Y-%m-%d %H:%M:%S"))
        state = time.time()-time_stamp
        if state >=0:
            return "停售｜仅供参考(请以秀动平台为准）"
        else:
            return "在售"
        
    
    def show_start_content_extract(self,response):
        
        try:
            null = response.xpath("//div[@class ='content']/h1/text()").extract()[0]
            return None
        except Exception as e:
            pass
        
        item = LivehouseItem()
        
        item['category'] = ','.join(response.xpath('//div[@class="label"]/label/text()').extract())
        item['show_name'] = response.xpath("//div[@class=\"describe\"]/div[@class='title']/text()").extract()[0]
        show_date = response.meta['date']
        if '时间：' in show_date:
            show_date = show_date.replace('时间：','')
        show_date = show_date.replace("/",'.')
        item['show_date'] = show_date
        """
        
        show_date = response.xpath("//div[@class=\"describe\"]/p/text()").extract()[0]
        if "演出时间：" in show_date:
            show_date = show_date.replace("演出时间：",'')
            show_date = show_date.replace('月','.').replace('年','.').replace('日','.').split('-')[0]
            item['show_date'] = show_date
        """
        
        artists_loc = response.xpath("//div[@class=\"describe\"]/p/a/text()").extract()
        item['city'],item['loc'] =artists_loc[-1].split(" ",1)
        item['shower'] = '|'.join(artists_loc[:-1])
        item['provider'] = "秀动"
        item['web'] = response.url
        item['sale_price'] = '|'.join(response.xpath("//div[@class = 'price-tags']/button/span/text()").extract())
        item['state'] = self.sale_state(response)
        item['target_shower'] = self.target_shower
        
        yield item
        
        return None
        
        
        
        
        
        
        
        