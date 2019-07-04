# 贪婪和非贪婪

import re

title = u'<div>name</div><div>age</div>'

# .匹配除换行符（\n、\r）之外的任何单个字符
# 贪婪模式
# .*代表任意字符0次或多次，一直会找到最后一个</div>
p1 = re.compile(r'<div>.*</div>')
# 非贪婪模式
# .*?，该处将前面的.*作为一个整体，匹配0次或者1次就结束了，所以找到第一个</div>就停止向后寻找匹配
p2 = re.compile(r'<div>.*?</div>')

m1 = p1.search(title)
print(m1)
print(m1.group())
print('*' * 50)

m2 = p2.search(title)
print(m2)
print(m2.group())
print('*' * 50)