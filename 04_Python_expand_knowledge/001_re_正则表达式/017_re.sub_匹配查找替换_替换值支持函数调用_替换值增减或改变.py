# -*- coding:utf-8 -*-

import re

def add(temp):
    strNum =temp.group()
    num = int(strNum) + 1
    return str(num)

# add自动调用上面的add函数，匹配的值处理后返回一个值
# 返回值替换掉字符串中的值
ret = re.sub(r'\d+', add, 'python = 999')
print(ret)
print('*' * 50)

ret = re.sub(r'\d+', add, 'python = 99')
print(ret)
print('*' * 50)
