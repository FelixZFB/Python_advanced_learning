# -*- coding:utf-8 -*-

# 在python中一切皆对象
# python中可以直接使用print，dict,list,他们都是内嵌函数
# 属于内嵌/内置函数，因此可以直接调用

dic = dict()

lis = list()

a = 100

def AAA():
    pass

# globals()可以查看所有的全局变量
print(globals())
# 输出结果可以发现，是一个键值字典
# 'dic': {}, 'lis': [], 'a': 100, 'AAA': <function AAA at 0x00000222BC92D268>
# 可以看见一些内置函数，文件的路径等等
# AAA函数就是一个AAA字符串键，值就是指向的画一个函数<function AAA at 0x00000222BC92D268>
# 字典中不能出现两个相同的键，因此函数中不能有相同的变量名
# 变量，函数，类的任何对象，名字不能相同
# 使用的时候，根据键的名字，去字典里面找对应的值-对象空间（对象会占用空间）

# '__builtins__': <module 'builtins' (built-in)>
# 上面内嵌函数调用的就是该模块
# 该模块中有什么函数查看002案例


# 上面就可以看出一切皆是对象