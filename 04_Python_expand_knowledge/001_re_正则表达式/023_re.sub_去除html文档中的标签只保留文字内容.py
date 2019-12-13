# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/13 10:38
Desc:
'''

import re

#去除标签

s = '''
    <div>\
    <p>岗位职责：</p>\
    <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>\
    <p><br></p>\
    <p>必备要求：</p>\
    <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>\
    <p>&nbsp;<br></p>\
'''

p = r"</?\w+>|&nbsp;"
print(re.sub(p, " ", s))
