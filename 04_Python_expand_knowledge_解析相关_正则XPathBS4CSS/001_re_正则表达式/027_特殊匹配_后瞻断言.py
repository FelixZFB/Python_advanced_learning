# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/13 14:06
Desc:
'''
import re

s = '98%1KK58%2AA65%3'


# 找出数字前面是%的数字
res = re.findall('(?<=%)\d+', s)
print(res)
print('*' * 50)

# 找出数字前面不是%的数字
res = re.findall('(?<!%)\d+', s)
print(res)
print('*' * 50)