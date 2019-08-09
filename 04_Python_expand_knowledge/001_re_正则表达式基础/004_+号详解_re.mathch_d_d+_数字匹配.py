# -*- coding:utf-8 -*-

import re

# \d用于用于匹配任意一个数字，等价于[0-9]、[0123456789]
# \d+匹配多个数字，等价于[0-9]+
# 注意：+号只针对于它前面的一个字符，[]也只代表一个字符
res = re.match(r'速度与激情\d', '速度与激情3')
print(res.group())

res = re.match(r'速度与激情[0-9]', '速度与激情7')
print(res.group())

res = re.match(r'速度与激情\d+', '速度与激情888')
print(res.group())

res = re.match(r'速度与激情[0-9]+', '速度与激情888')
print(res.group())
print('*' * 50)

# 只匹配几个数字,匹配0-2和7-9的数字，连着写，2和7之间不需要空格，空格就是匹配空格符号了
res = re.match(r'速度与激情[0-27-9]', '速度与激情588')
print(res)

res = re.match(r'速度与激情[0-27-9]+', '速度与激情77 9')
print(res)
print(res.group())
print('*' * 50)

res = re.match(r'速度与激情+[0-2 7-9]+', '速度与激情情77 9')
print(res)
print(res.group())
print('*' * 50)