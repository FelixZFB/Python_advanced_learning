# -*- coding:utf-8 -*-

import re

# - re.search 扫描整个字符串并返回第一个成功的匹配
# re.search(pattern, string, flags=0)

ret = re.search(r'\d+', '阅读次数999好的')
print(ret.group())
print('*' * 50)

# 只会匹配返回第一个
ret = re.search(r'\d+', '阅读次数999好的111')
print(type(ret))
print(ret.group())
print('*' * 50)

# 要匹配所有的用findall
ret = re.findall(r'\d+', '阅读次数999好的111')
print(type(ret))
print(ret)
print('*' * 50)