# -*- coding: utf-8 -*-
# Page49

# 插入字符串，将字符串插入到给定的字符串之中

str1 = "Python"

# 字符串当做一个整体插入到给定符号字符之间
str2 = str1.join('----')
print(str2)

# 插入到字母之间
str3 = str1.join('HI')
print(str3)

# 只有一个字符，无法插入，返回新的字符
str4 = str1.join('H')
print(str4)