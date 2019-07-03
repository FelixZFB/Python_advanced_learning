# -*- coding:utf-8 -*-

import re

res = re.match(r'hello', 'hello, world!')
# 匹配结果
print(res)
# 取出匹配的结果，span表示取出的字符的范围
print(res.group())
print('*' * 50)

# []中括号，匹配中括号里面的任意一个字符都可以
# 匹配小的h或者大写的H
res = re.match(r'[hH]ello', 'Hello, world!')
# 匹配结果
print(res)
# 取出匹配的结果
print(res.group())
print('*' * 50)


# \d用于用于匹配任意一个数字，等价于[0-9]、[0123456789]
res = re.match(r'速度与激情\d', '速度与激情3')
print(res)
print(res.group())
print('*' * 50)

# 注意使用，match匹配，表达式会从字符串第一个字符开始匹配
# 如果匹配不上则是找不到结果，结果为None
res = re.match(r'速度与激情\d', '电影速度与激情7')
print(res)
print('*' * 50)