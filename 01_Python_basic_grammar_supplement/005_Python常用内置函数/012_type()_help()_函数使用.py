# -*- coding:utf-8 -*-

# type内置函数本来是查看变量类型的一个函数
# 但是type在较早版本有一个创建动态类的功能
# 为了保持兼容性，该功能仍然保留在
# 正常情况一个函数，只应该有一种功能

# 定义一个类，并创建一个实例对象
class A():
    pass
aaa = A()

# 查看类和实例对象的的类型
print(type(A))
print('*' * 50)
print(type(aaa))
print('*' * 50)
# 我们可以发现类的类型就是type，是不是很神奇


# 其实，type不是一个函数，而是一个类，我们可以查看其类型
print(type(type))
print('*' * 50)
# help（）函数可以查看一个函数的描述和里面其它的各种信息
# 我们也可以使用ctrl然后查看源码，type就是位于builtins.py中的一个类
print(help(type))
print('*' * 50)



