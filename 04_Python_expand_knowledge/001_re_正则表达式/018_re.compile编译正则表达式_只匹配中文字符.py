# -*- coding:utf-8 -*-

import re

# \w：匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# 注意，\w也可以匹配中文，慎用。

# 如果只匹配中文字符[\u4e00-\u9fa5],代表中文字符


title = '世界 你好，hello world'

# 匹配中文字符，找出所有的中文字符
p = re.compile(r'[\u4e00-\u9fa5]+')
rst1 = p.findall(title)
print(rst1)
print('*' * 50)

# 推荐下面的标准写法，表达式太长，
# 可以先编写正则表达式,使用上面的写法
rst1 = re.findall(r'[\u4e00-\u9fa5]+', title)
print(rst1)
print('*' * 50)

# 以下方式匹配只从第一个字符开始，+匹配一次或多次，匹配到第一个符合条件的就结束向后查找
rst2 = re.match(r'[\u4e00-\u9fa5]+', title)
print(rst2[0])
print('*' * 50)