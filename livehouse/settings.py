# -*- coding: utf-8 -*-

# Scrapy settings for livehouse project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'livehouse'

#LOG_LEVEL = 'WARNING'
#LOG_FILE = './log.log'

SPIDER_MODULES = ['livehouse.spiders']
NEWSPIDER_MODULE = 'livehouse.spiders'

mysql_host = 'localhost'
mysql_database = 'livehouse'
mysql_port = 3306
mysql_user = "root"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'livehouse (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False



showstart_location_code_dict = {
    '':'',
    2:"摇滚",26:"独立",1:"民谣",6:"HipHop",3:"流行",23:'朋克',
    12:"金属",19:"脱口秀",5:"轻音乐",25:"核",4:"电子",21:"话剧歌剧",7:"古典",
    8:"世界音乐",11:"动漫",13:"布鲁斯",18:"实验",28:"放克",30:"曲苑杂坛"
                                }

showstart_live_type_code = [2,26,1,23,3,12,25,4,8,13,18,28,3]

showstart_type_code_dict = {}

damai_url = 'https://search.damai.cn/searchajax.html?keyword={shower}&cty={city}&ctl=&sctl=&tsg=0&st=&et=&order=0&pageSize=30&currPage={currpage}&tn='
"""
damai_headers = {
    'Host': 'search.damai.cn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-length': '83',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://search.damai.cn',
    'referer': 'https://search.damai.cn/search.htm?spm=a2oeg.home.card_0.dviewall.591b23e1iGKd0T&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=%E6%88%90%E9%83%BD',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookies':"isg=BBkZNRdmnNuygEBPaBgE0dmGKgPzpg1Y461mDzvNZsKiQjnUg_USKAcbRIY0YaWQ; l=eBT8dxycgiDVErKJBO5Bourza779WQd04kPzaNbMiIncC6bF94JdxWtQcqytodKRRLXAGe8B4lwUWUe9-etf96HmndnNZ2URZcHDB; tfstk=cVsCBN42N_IwEzmre9wZaHQ7IKx5a1mBQJOGdaGgV3tsOojHBsA7gIVk8TcOhnJ1.; XSRF-TOKEN=8220154d-11cb-4846-85cd-f15a5110cefa; xlly_s=1; cna=ZrHaGY0uGy8CAbfsE5fD6HkP"
}
"""
damai_headers = {
            "cookie": "isg=BNnZ8Xt83Bysg4CPqFjEkRnG6sOzZs0Yo22mT_uUkYQWAv6Ub7Ws6HRTBEZ0oWVQ; l=eBT8dxycgiDVECTOBO5BFurza779rURcfkPzaNbMiIncC6mA6Rp-e2KQc4GzkpKRRLXAGn9X4lwUWUetTFv77sDmndLnX9IlYxDDU; tfstk=cE9VBOqPsOYS5BWdnt6ZCZ4j34yACWJHBzS1iIApO7E347k5fE5cPAI5WbCPOLGfi; x_hm_tuid=NJLtxKtXl3iYFMT24yqr2oyXzCyPJMtyePS7SSv+ztkJBRfUq4azMjSIq2GIOyjH; XSRF-TOKEN=8220154d-11cb-4846-85cd-f15a5110cefa; xlly_s=1; cna=ZrHaGY0uGy8CAbfsE5fD6HkP",
            "referer": "https://search.damai.cn/search.htm?ctl=%20%20%20&order=1&cty="
        }
"""
damai_data = {
    'keyword': '',
    'cty': '',
    'ctl': '',
    'currPage': '1',
    'singleChar': '',
    'tn': '',
    'sctl': '',
    'tsg': '0',
    'order': '1',
}
"""
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'livehouse.middlewares.LivehouseSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'livehouse.middlewares.LivehouseDownloaderMiddleware': 543,
    "livehouse.middlewares.RandomUserAgentMiddleware":544
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'livehouse.pipelines.LivehousePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
