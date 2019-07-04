# -*- coding:utf-8 -*-

import re

# \w：匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'
# \number: \1 或\2 ...，用于匹配和前面分组一模一样的内容
# 最常用于网页源码标签的匹配（标签都是成对出现）

# 标签匹配
html_str = '<h1>hello, world!</h1>'
ret = re.match(r'<\w*>.*</\w*>', html_str)
print(ret.group())
print('*' * 50)

# 上面的写法标签不相同，也可以匹配
html_str = '<h1>hello, world!</body>'
ret = re.match(r'<\w*>.*</\w*>', html_str)
print(ret.group())
print('*' * 50)

# 为了限制前后匹配的标签一致，就可以使用小括号()分组和\num匹配前面的分组
# \1就代表匹配与第一个分组(\w*)匹配到的结果要一模一样
html_str = '<h1>hello, world!</h1>'
ret = re.match(r'<(\w*)>.*</\1>', html_str)
print(ret.group())
print('*' * 50)

# 进行两个分组，使用\1 \2,类似位置参数
# 注意\1 \2 位置不要写反了，写反了就匹配不到了
html_str = '<body><div>hello, world!</div></body>'
ret = re.match(r'<(\w*)><(\w*)>.*</\2></\1>', html_str)
print(ret.group())
print('*' * 50)


