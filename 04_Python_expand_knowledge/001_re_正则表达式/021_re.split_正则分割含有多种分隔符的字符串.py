# -*- coding:utf-8 -*-

# 含有多种分隔符分割

# 正则表达式分割,推荐使用
import re
# 将多个分隔符直接写在正则表达式中，使用中括号，后面的+号表示前面的符号可以出现多次
# 中括号每个字符都是一个匹配
s = 'ab;cd%e\tfg,,jklioha;hp,vrww\tyz'
t = re.split(r'[;%,\t]+', s)
print(t)


# 上面可以使用中括号也可以使用竖线
ret = re.split(r":|%| ","info:xiao%Zhang 33 shandong")
print(ret)
