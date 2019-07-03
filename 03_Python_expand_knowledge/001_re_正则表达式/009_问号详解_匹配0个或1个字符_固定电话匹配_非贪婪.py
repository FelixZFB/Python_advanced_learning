# -*- coding:utf-8 -*-

import re

# ?	匹配0个或1个由问好前面字符或者表达式，
# 非贪婪方式(?号前面的一个字符)

# 匹配座机电话号码，匹配-0次或者1次
res = re.match(r'021-?\d{8}', '021-84587895')
print(res)
print(res.group())
print('*' * 50)

res = re.match(r'021-?\d{8}', '02184585895')
print(res)
print(res.group())
print('*' * 50)

# 全国座机电话判断,区号有些三位有些四位，电话号码有些8位或7位
res = re.match(r'\d{3,4}-?\d{7,8}', '0717-7640999')
print(res)
print(res.group())
print('*' * 50)