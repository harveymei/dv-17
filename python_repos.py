#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/19 11:04 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: python_repos.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)

response_dic = r.json()

print(response_dic.keys())
