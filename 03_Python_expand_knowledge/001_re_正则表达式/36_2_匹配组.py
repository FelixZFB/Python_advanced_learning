import re

# re.I忽略大小写
# 两个组，两个组中间有一个空格
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = p.match("I am really love wangxiaojing")
print(m)
# 打印出匹配到的所有对象
print(m.groups())

# 给的参数为0，默认是匹配到的对象，整个组
print(m.group(0))
print(m.start(0))
print(m.end(0))
print(m.span(0))

# 参数为1，组中的第一个对象
print(m.group(1))
print(m.start())
print(m.end(1))
print(m.span(1))
