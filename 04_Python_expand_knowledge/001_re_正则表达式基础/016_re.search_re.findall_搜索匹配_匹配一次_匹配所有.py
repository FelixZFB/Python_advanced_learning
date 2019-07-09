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

# 如果search或findall里面有小括号编组，返回的则是编组的内容编组的内容组成一个列表
# 有多个编组，返回一个元组组成的列表，元组里面放置每个编组
ret = re.findall(r'(好的)(\d+)', '阅读次数999好的111次数999好的333')
print(type(ret))
print(ret)
print('*' * 50)

# 爬虫正则匹配时候，提取属性里面的网址
html= 'data-mp4="http://mvideo.spriteapp.cn/video/2019/0704/5d1df3431923c_wpcco.mp4"'
url = re.findall(r'data-mp4="(.*?)"', html)
print(url)
