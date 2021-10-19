# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import DropItem


class LivehousePipeline:
    
    def __init__(self):
        
        return None
    
    def open_spider(self,spider):
        #连接数据库
        
        self.db = pymysql.connect(
            host = 'localhost',
            user = "root",
            password = "841658601pbl",
            database = 'livehouse',
            port = 3306,
            charset = 'utf8',
            ssl = {'ssl':{}}
            )
        self.cursor = self.db.cursor()        
        
        return None
        
    def close_spider(self,spider):
        self.db.close()
        return None
    """这里不知为何行不通，后面直接传参数了
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get("mysql_host"),
            database=crawler.settings.get("mysql_database"),
            user = crawler.settings.get("mysql_user"),
            password = crawler.settings.get("mysql_pass"),
            port = crawler.settings.get("mysql_port"),
            )
 """   
    def process_item(self, item, spider):
        
        data = dict(item)
        keys = ",".join(data.keys())
        values = ",".join(['%s']*len(data))
        if item['target_shower']  in item['shower']:
            sql  = ' insert  into  %s  (%s)  values  (%s )'%  ('livehouse',  keys,  values)
            self.cursor.execute(sql,  tuple(data.values()))
            self.db.commit()
        else:
            raise  DropItem(f"Missing price in {item}")
        
        return item
