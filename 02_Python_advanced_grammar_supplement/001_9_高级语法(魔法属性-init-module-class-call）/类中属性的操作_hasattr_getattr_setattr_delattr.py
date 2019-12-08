# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/7 17:49
Desc:
'''

class function_demo(object):
    name = 'demo'
    def run(self):
        return "hello function"
functiondemo = function_demo()
res1 = hasattr(functiondemo, "name") # 判断对象是否有name属性，True
res2 = hasattr(functiondemo, "run") # 判断对象是否有run方法，True
res3 = hasattr(functiondemo, "age") # 判断对象是否有age属性，False
print(res1, res2, res3)

# 删除属性，
res4 = delattr(function_demo, 'name')
res5 = hasattr(functiondemo, "name")
print(res4, res5)