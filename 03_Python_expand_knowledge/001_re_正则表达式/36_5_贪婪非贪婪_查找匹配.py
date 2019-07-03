# 贪婪和非贪婪

import re
title = u'<div>name</div><div>age</div>'

# .匹配除换行符（\n、\r）之外的任何单个字符
# 贪婪模式
p1 = re.compile(r'<div>.*</div>')
# 非贪婪模式
p2 = re.compile(r'<div>.*?</div>')

m1 = p1.search(title)
print(m1)
print(m1.group())
print(m1.groups())


m2 = p2.search(title)
print(m2)
print(m2.group())
print(type(m2.groups()))