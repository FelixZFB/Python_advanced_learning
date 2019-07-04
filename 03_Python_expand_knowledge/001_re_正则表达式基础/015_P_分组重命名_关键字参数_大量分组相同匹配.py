# -*- coding:utf-8 -*-

import re

# P重命名了解，一般位置匹配够用了

# (?P<name>分组的内容)    ?P<name> 用于给分组起别名，类似于关键参数
# (?P=name)或者(\g<name>) 引用别名为name分组匹配到的字符串, 引用上面的关键字参数的组，匹配一模一样的字符

# 分组重命名匹配，如果相同标签或字符的分组特别多，使用\1 \2 \3就会容易找不到位置
# 因此，可以对每个分组重命名，分组里面加上?P<name>即可
# 后面使用该分组时，分组里面使用?P=name
# 注意，前后相同匹配都需要使用分组，小括号
html_str = '<body><div>hello, world!</div></body>'
ret = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', html_str)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
print(ret.group('name1'))
print(ret.group('name2'))
print('*' * 50)

