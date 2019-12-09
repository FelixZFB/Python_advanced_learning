# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/9 15:16
Desc:
'''

# 保证只有一个对象。
# 注意：在python中导入模块就是一种单例模式。

class People(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            return cls.instance
        else:
            return cls.instance


per1 = People()
per2 = People()
# 没有重写new前，id不同
print(id(per1))  # 1804447642344
print(id(per2))  # 1804447642344
