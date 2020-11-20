# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/12 16:11
Desc:
'''
import re

# 特殊情况，表达式中含有.*?，但是?和前面的*间隔一个字符在后面不在一起，
# ?只表示匹配它前面的那个字符0次或1次，此处有特殊，看下面案例
# 都是贪婪匹配，?后面可以看做实际写了一个.*，最大匹配
# 如果结尾是?号，直接匹配到末尾
# 如果?号后面还有字符，直接匹配到最后一个符合条件的字符
print('特殊情况：')

html1 = '<H1>Chapter<H1><H1>Chapter<H1>555END'

res = re.match(r'<.*>5', html1) # <H1>Chapter<H1><H1>Chapter<H1>5
print(res.group())

res = re.match(r'<.*>?5', html1) # <H1>Chapter<H1><H1>Chapter<H1>555
print(res.group())

res = re.match(r'<.*>?N', html1) # <H1>Chapter<H1><H1>Chapter<H1>555EN
print(res.group())

res = re.match(r'<.*>?', html1) # <H1>Chapter<H1><H1>Chapter<H1>555END
print(res.group())

res = re.match(r'<.*>?.*', html1) # <H1>Chapter<H1><H1>Chapter<H1>555END
print(res.group())

res = re.match(r'<.*>5?', html1) # <H1>Chapter<H1><H1>Chapter<H1>5
print(res.group())

res = re.match(r'<.*5?', html1) # <H1>Chapter<H1><H1>Chapter<H1>555END
print(res.group())