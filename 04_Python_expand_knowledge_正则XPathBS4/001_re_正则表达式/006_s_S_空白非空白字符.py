# -*- coding:utf-8 -*-

import re

# \s: 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [\f\n\r\t\v]。
# \S: 匹配任何非空白字符。等价于 [^\f\n\r\t\v]。
# 较少使用

res = re.match(r'速度与激情\s\d+', '速度与激情 3')
print(res)
print(res.group())
print('*' * 50)

# \t制表符
res = re.match(r'速度与激情\s\d+', '速度与激情\t3')
print(res)
print(res.group())
print('*' * 50)

# \n换行符
res = re.match(r'速度与激情\s\d+', '速度与激情\n3')
print(res)
print(res.group())
print('*' * 50)