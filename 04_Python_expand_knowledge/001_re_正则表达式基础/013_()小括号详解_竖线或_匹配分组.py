# -*- coding:utf-8 -*-

import re

# |:匹配左右任意一个表达式，类似于or或
# () 是为了提取匹配的字符串。
# 表达式中有几个()就有几个相应的匹配字符串,一个()代表一个组。


# 小括号里面内容当做一个整体，是一个分组
# |前后作为一个表达式，类似于或，既可以匹配163，也可以匹配126
# group()和group(0)默认取出第一个分组，就是匹配的整体
# 多少小括号就有多少个分组
ret = re.match(r'[a-zA-Z0-9]{6,12}@(163|126|qq)\.com$', 'laowang@qq.com')
print(ret)
print(ret.group())
print(ret.group(0))
print(ret.group(1))
print('*' * 50)

# 两个分组，第一个分组1，第二个分组2
ret = re.match(r'([a-zA-Z0-9]{6,12})@(163|126|qq)\.com$', 'laowang@126.com')
print(ret)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
# groups可以取出每一个分组，结果是一个元组
print(ret.groups())
print('*' * 50)