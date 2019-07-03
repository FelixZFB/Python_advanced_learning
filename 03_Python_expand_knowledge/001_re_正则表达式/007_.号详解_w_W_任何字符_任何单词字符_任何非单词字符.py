# -*- coding:utf-8 -*-

import re

# .：匹配除 "\n" 之外的任何单个字符,匹配最广的符号
# 要匹配包括 '\n' 在内的任何字符，请使用'[.\n]' 的模式。

# \w：匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# 注意，\w也可以匹配中文，慎用。
# \W：匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'

# 任意字符
res = re.match(r'速度与激情.', '速度与激情p3')
print(res)
print(res.group())
print('*' * 50)

# 任意多个字符
res = re.match(r'速度与激情.+', '速度与激情-3a哈哈')
print(res)
print(res.group())
print('*' * 50)