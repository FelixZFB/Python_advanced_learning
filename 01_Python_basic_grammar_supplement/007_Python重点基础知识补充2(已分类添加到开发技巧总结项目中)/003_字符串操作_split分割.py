# -*- coding: utf-8 -*-
# Page49

# 分割字符串，分割依据是字符串内部的字符，可以是字母，也可以是空格，逗号等

str1 = "Python is wonderful!"

# 默认以字符串内部的空格分割字符,分割结果是一个列表
str2 = str1.split()
print(str2)

# 以空格分割，但是只分割1次
str3 = str1.split(None, 1)
print(str3)

# 以字母O分割字符串
str4 = str1.split('o')
print(str4)

