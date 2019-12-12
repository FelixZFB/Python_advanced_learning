# -*- coding:utf-8 -*-
import re

names = ['name1', '_name', 'name_1_1', '2_name', '_name_', '#_name_','name?_', 'name!']

for name in names:
    # 注意：\w等价于[A-Za-z0-9_]，但是可以匹配中文字符
    # 变量名字母或者下划线开头(不能数字开头)
    # 字母数字下划线结尾
    # [a-zA-Z_]:判断第一位一定只能是字母或者下划线
    # [a-zA-Z0-9_]*:第二位开始只能是字母数字下划线，可以出现0次或多次
    # $：检测到字符串的结尾,最后一个符合的字符也是字符串的结尾
    # ^: 判断开头，match默认从开头开始判断，所以可以不写
    res = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name)
    if res:
        print("变量名 %s 符合要求" % res.group())
    else:
        print("变量名 %s 非法" % name)