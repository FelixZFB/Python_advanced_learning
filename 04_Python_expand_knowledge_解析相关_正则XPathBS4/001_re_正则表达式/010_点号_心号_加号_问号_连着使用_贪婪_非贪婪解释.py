# -*- coding:utf-8 -*-

import re

# .*：贪婪匹配，找到满足条件的最大匹配
# .*?：非贪婪，找到满足条件的最小匹配
# .+?：非贪婪，找到满足条件的最小匹配
# ?非贪婪一般都是放在*和+号后面使用
# 经常是：.* .+  \d+  此时它们都当做一个整体，匹配到0次或者1次即可。
# 看下面实例：


# .*贪婪匹配使用：
# .匹配出空格\n之外的任何字符，*匹配0次或多次，就是任意次，+匹配1次或多次
# 从头开始匹配到<,.*任意字符，一直找到结尾，匹配到最后一个>
# 虽然前面也有>,但是>也是任意字符，但是还会继续向后找，
# 一直找到最后一个满足要求的字符串
# 这就是贪婪匹配,最终结果：<H1>Chapter<H1><H1>Chapter<H1>
html = '<H1>Chapter<H1><H1>Chapter<H1>END'
res = re.match(r'<.*>', html)
print(res)
print(res.group())
print('*' * 50)

res = re.match(r'<.+>', html)
print(res)
print(res.group())
print('*' * 50)

# 非贪婪，?后面有一个>，会找到第一个满足表达式的匹配就结束匹配
res = re.match(r'<.*?>', html)
print(res)
print(res.group())
print('*' * 50)

# 非贪婪，?后面有一个>，会找到第一个满足表达式的匹配就结束匹配
res = re.match(r'<.+?>', html)
print(res)
print(res.group())
print('*' * 50)


# 非贪婪\d+?,\d+当做一个整体，实际就是匹配一个数字
# ?匹配它前面的字符0次或者1次
# 下面三种写法结果都一样：
html1 = '<H1>Chapter<H1><H1>Chapter<H1>555END'
res = re.match(r'<.*>\d', html1)
print(res.group())

res = re.match(r'<.*>\d?', html1)
print(res.group())

# 本来是想匹配多个数字，但是后面有一个?，还是最小匹配1次
res = re.match(r'<.*>\d+?', html1)
print(res.group())

# 匹配多个数字
res = re.match(r'<.*>\d+', html1)
print(res.group())
print('*' * 50)


