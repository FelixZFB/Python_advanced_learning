# -*- coding:utf-8 -*-

import re

# re.sub用于替换字符串中的匹配项,匹配到的内容全部替换
# 先进行findall查找匹配，然后进行替换，最后返回结果
# re.sub(pattern, repl, string, count=0)


# sub替换案例
# 删除注释
phone = "2004-959-559 # 这是一个电话号码"
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)
print('*' * 50)


# 移除非数字的内容,\D非数字内容，全部替换
phone = "2004-959-559 # 这是一个电话号码"
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)
print('*' * 50)