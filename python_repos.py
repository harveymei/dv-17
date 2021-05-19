#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/19 11:04 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: python_repos.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import requests

# 执行api调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)

# 将api响应存储在变量中
response_dic = r.json()  # 使用方法json()将这些信息转换为一个Python字典

# 打印字典中的key
# print(response_dic.keys())
# 打印总项目仓库数量
print("Total repositories: ", response_dic['total_count'])

# 将字典中items键对应的列表值赋值变量（列表中包含多个字典）
repo_dicts = response_dic['items']
print("Repositories returned:", len(repo_dicts))  # 计算字典数量（返回的项目字典数量）

# 取项目列表中第一个字典中赋值变量
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))  # 打印当前项目字典中键值对的数量
for key in sorted(repo_dict.keys()):  # 排序并打印当前项目字典中的键
    print(key)

