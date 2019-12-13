# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/13 12:37
Desc:
'''
import re

# x(?=y)称为先行断言（Positive look-ahead），x只有在y前面才匹配，y不会被计入返回结果
# 也可以理解为x后面必须是y,一般用于匹配以什么结尾

# “先行断言”中，括号里的部分是不会返回的
# 匹配结果和分组取出的结果都不会包含括号中的内容
s = '98%1KK58%2AA65%3'
res = re.match('\d+(?=%)', s)
print(res)
print(res.groups())
print('*' * 50)

# 如果先行断言后面还有匹配内容，匹配结果里面会包含括号中内容
res = re.match('\d+(?=%).*', s)
print(res)
print(res.groups())
print('*' * 50)


# 先行断言和先行否定断言都是取出来的断言表达式的匹配结果
# 找出以%结尾的所有数字
res = re.findall('\d+(?=%)', s)
print(res)
print('*' * 50)

# 找出所有不是以%结尾的数字
res = re.findall('\d+(?!%)', s)
print(res)
print('*' * 50)


# 先行否定断言
# 找出后面结尾不是.的所有数字
s1 = '3.1415.444'
res = re.findall('\d+(?!\.)', s1)
print(res)
print('*' * 50)