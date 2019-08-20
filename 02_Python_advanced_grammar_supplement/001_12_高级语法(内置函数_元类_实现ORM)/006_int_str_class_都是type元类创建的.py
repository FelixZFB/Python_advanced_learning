# -*- coding:utf-8 -*-

# 对象的__class__方法可以查看对象是属于哪个类


class A():
    pass

print(int.__class__)
print(str.__class__)
print(A.__class__)
print('*' * 50)

# 运行结果显示，字符串，整数，类都是属于type元类

a = 100
# a属于int类，int类属于type元类
print(type(a))
print(a.__class__)
print(a.__class__.__class__)
print('*' * 50)

# **************************************************
# <class 'int'>
# <class 'int'>
# <class 'type'>
# **************************************************

# 在python2中上面输出结果应该是<type 'int'>
# 在python3以后type都改成class为了更加清晰的区分

# 元类就是创建类这种对象的东西。type就是Python的内建元类，
# 当然了，你也可以创建自己的元类。
