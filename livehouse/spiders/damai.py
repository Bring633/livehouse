import scrapy
from livehouse.items import LivehouseItem
import livehouse.settings as settings
import json
import time
import random
import requests

class DamaiSpider(scrapy.Spider):
    name = 'damai'
    allowed_domains = ['damai.cn']
    start_urls = ['https://search.damai.cn/searchajax.html']

    def __init__(self,start_date=None,end_date = None,loc='',shower=''):

        self.start_date = start_date
        self.end_date = end_date
        self.loc = loc
        self.shower = shower
        self.target_shower = shower
        
        return None
    
    def start_requests(self,):
        
        headers = settings.damai_headers
        
        url = settings.damai_url.format(shower = self.shower,city = self.loc,currpage = 1)
        
        res = requests.get(url,headers = settings.damai_headers).text
        
        res_json = json.loads(res)
        
        next_page = res_json['pageData']["nextPage"]
        
        if 1 != next_page:
            url = settings.damai_url.format(shower = self.shower,city = self.city,currpage = next_page)
            yield scrapy.Request(url,method = 'get',headers = headers,callback =self.continue_request ,meta = {'currpage':next_page},dont_filter=True)        
        else:
            pass
        
        page_id = res_json['ids'].split(',')

        item = LivehouseItem()
        
        data = res_json['pageData']['resultData']
        base_url = 'https://detail.damai.cn/item.htm?&id='
        
        for i in range(len(data)):
            
            item = LivehouseItem()
            
            item_url = base_url+page_id[i]
            
            item['category'] = data[i]['categoryname']
            shower = data[i]['actors'].replace('<span class=\"c4\">','').replace('</span>','').replace('、',"|")
            if '艺人：' in shower:
                shower = shower.replace('艺人：','')
                item['shower'] = shower
            item['city'] = data[i]['cityname']
            item['show_name'] = data[i]['name']
            item['loc'] = data[i]['venue']
            item['state'] = data[i]['showstatus']
            item['provider'] = '大麦'
            item['web'] = item_url
            item['target_shower'] = self.target_shower
            
            time.sleep(0.1+random.random())
            
            yield scrapy.Request(item_url,callback=self.content_parse,meta={'data':item},dont_filter=True)
        
        
        return None
    
    def continue_request(self,response):
        
        res_json = json.loads(response.text)
        
        next_page = res_json['pageData']["nextPage"]
        
        headers = settings.damai_headers
        
        if response['currpage'] != next_page:
            url = settings.damai_url.format(shower = self.shower,city = self.city,currpage = next_page)
            yield scrapy.Request(url,method = 'get',headers = headers,callback =self.continue_request ,meta = {'currpage':next_page},dont_filter=True)        
        else:
            pass
        
        return None
        
        

    def parse(self, response):
        
        item = LivehouseItem()
        page_id = response.meta['page_id'].split(',')
        
        data = json.loads(response.text)['pageData']['resulatData']
        
        base_url = 'https://item.damai.cn/item/project.htm?id='
        
        for i in len(data):
            
            item = LivehouseItem()
            
            item_url = base_url+page_id[i]
            
            item['category'] = data[i]['categoryname']
            item['shower'] = data[i]['actors'].replace('<span class=\"c4\">','').replace('</span>','').replace('、',"|")
            item['city'] = data[i]['cityname']
            item['show_name'] = data[i]['name']
            item['loc'] = data[i]['venue']
            item['state'] = data[i]['showstatus']
            item['provider'] = '大麦'
            item['web'] = item_url
            item['target_shower'] = self.target_shower
            
            time.sleep(0.1+random.random())
            
            yield scrapy.Request(item_url,callback=self.content_parse,meta={'data':item},dont_filter=True)
        
        return None
    
    def content_parse(self,response):
        
        item = response.meta['data']
        
        try:
            new_data = json.loads(response.xpath('//div[contains(@id,"dataDefault")]/text()').extract()[0])['performBases'][0]['performs'][0]
        except Exception as e:
            print(e)
            return None
        
        item['show_date'] = new_data['performTime']
        price = new_data['skuList']
        price_len = len(price)
        price_list = []
        for i in range(price_len):
            price_list.append(price[i]['skuName'])
        item['sale_price'] = '|'.join(price_list)
        
        yield item
        
        return None
        















