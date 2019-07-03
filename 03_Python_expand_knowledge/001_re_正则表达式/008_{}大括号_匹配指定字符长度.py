# -*- coding:utf-8 -*-

import re

# - {}一般用来表示匹配的长度，只限制{}它前面的一个字符
# 比如 \d{3} 表示匹配三个连续数字，\d{1,3}表示匹配一到三个数字，包括1和3。
# 注意：逗号后面不要加空格

res = re.match(r'\d{3}', '12345')
print(res)
print(res.group())
print('*' * 50)

res = re.match(r'\d{1,4}', '12345')
print(res)
print(res.group())
print('*' * 50)