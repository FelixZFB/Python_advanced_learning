# -*- coding:utf-8 -*-

import re

# []用来匹配多个数字多个字母,匹配任何一个都可以
# 注意：中括号里面的所有表达式只匹配一个就结束，中括号只代表一个字符
res = re.match(r'速度与激情[1-9a-zA-Z]', '速度与激情3aA')
print(res)
print(res.group())
print('*' * 50)

# 匹配多个，后面使用一个[]+
res = re.match(r'速度与激情[1-9a-zA-Z]+', '速度与激情3aA')
print(res.group())
print('*' * 50)

# 匹配多个，匹配多次，后面使用一个[]+
# [1-9a-zA-Z]+可以匹配到任何数字和字母
res = re.match(r'速度与激情[1-9a-zA-Z]+', '速度与激情3A5a8')
print(res.group())
print('*' * 50)

# 不连续的情况，可以使用多个[]括号分开写
# 注意+号只针对于它前面的一个字符，[]代表一个字符
res = re.match(r'速度与激情[1-9a-zA-Z]+速度[1-9a-zA-Z]+', '速度与激情3A5速度a8')
print(res.group())
print('*' * 50)

# [^Aa]匹配出A和a以外的任何字符,下面找出除Aa以外的所有字符
# 使用的findall就会找出所有匹配的分组
res = re.findall(r'[^Aa]+', '速度与激情3A5速度a8')
print(res)
print('*' * 20)

# match只会匹配到第一个就结束，从头开始，到A的时候就结束了
res = re.match(r'[^Aa]+', '速度与激情3A5速度a8')
print(res.group())
print('*' * 20)