# -*- coding:utf-8 -*-

import re

# *	匹配0个或多个的表达式,贪婪模式(*号前面的一个字符)。

# 贪婪匹配
html = 'dfajt\nfaueiun\nfhha\tlfkjl'
print(html)
print('*' * 50)

# .匹配任何字符，除了\n
res = re.match(r'.*', html)
print(res)
print(res.group())
print('*' * 50)

# 上面字符串中有特殊字符，可以加水re.S参数
# re.S参数代表前面的字符串是一个整体，里面的特殊字符都是普通字符
# \n \t都是普通字符，去掉\的转义含义
res = re.match(r'.*', html, re.S)
print(res)
print(res.group())
print('*' * 50)


