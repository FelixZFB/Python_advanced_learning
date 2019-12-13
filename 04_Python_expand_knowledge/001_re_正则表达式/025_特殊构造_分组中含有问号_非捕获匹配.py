# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/13 11:20
Desc:
'''
import re

s = '今天星期5,我们干嘛去'

res = re.match('今天(?:星期)(.*)', s)
print(res)
print(res.groups())

# 正常捕获匹配
s1 = 'http://google.com/index'
res = re.match('(http|ftp)://([^/\r\n]+)(/[^\r\n]*)?', s1)
print(res)
print(res.groups())
print('*' * 50)

# 非捕获匹配
s1 = 'http://google.com/index'
res = re.match('(?:http|ftp)://([^/\r\n]+)(/[^\r\n]*)?', s1)
print(res)
print(res.groups())
print('*' * 50)

# 正常捕获，一个正则表达式是正常匹配，第一个括号返回网络协议；
# 后一个正则表达式是非捕获匹配，返回结果中不包括网络协议。