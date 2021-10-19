#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:44:22 2021

@author: bring
"""

import requests
from settings import *
import json

url = 'https://search.damai.cn/searchajax.html?keyword=%E5%9B%9E%E6%98%A5%E4%B8%B9&cty=&ctl=&sctl=&tsg=0&st=&et=&order=0&pageSize=30&currPage=1&tn='

res = requests.get(url,data = damai_data,headers = damai_headers)
data = json.loads(res.text)

#%%

