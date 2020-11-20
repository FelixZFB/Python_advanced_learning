# 正则的使用,match匹配的案例

import re

# 两个小括号为两个组，中间要有一个空格
# 中括号中a-z,可以匹配a-z中的任何字母,
# 后面的+号为匹配一次或者多次
# 例如'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"
# 该处就是可以匹配一个完整的单词
s = r'([a-z]+) ([a-z]+)'

# 正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
# 修饰符被指定为一个可选的标志。
# 多个标志可以通过按位 OR(|) 它们来指定。如 re.I|re.M 被设置成I和M标志
# re.I 使匹配对大小写不敏感,忽略大小写
pattern = re.compile(s, re.I)
m = pattern.match('Hello world wide web')

# group(0)表示匹配成功的整个字符串
s = m.group()
print(s)
print(m.group(0))

# 返回一个tuple对象
print(m.groups(0))

# 返回匹配成功字符串的跨度，即开始位置和结束位置
a = m.span(0)
print(a)
print(m.start(0))
print(m.end(0))

# group(1)表示返回的第一个匹配的的小组
print(m.group(1))
print(m.group(2))
print(m.groups())


