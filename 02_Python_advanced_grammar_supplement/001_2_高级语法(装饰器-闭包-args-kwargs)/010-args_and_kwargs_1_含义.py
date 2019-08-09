# -*- coding: utf-8 -*-

# *args: 允许函数 传入多个不定量个数的非关键字参数，传入方式元组
# 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，
# args是元组类型，这就是包裹位置参数传递

# **kwargs: 允许函数传入多个不定量个数的关键字参数，传入方式字典
# 关键字参数：用于函数的调用，通过“键-值”的形式
# kwargs是一个字典(dict)，收集所有关键字参数,包裹关键字参数传递

# *和**代表多个的意思，多个参数

# 传入位置参数和关键字参数
# 一个关键字直接使用等号，多个关键字参数加使用字典，前面加**
def may_function(*args, **kwargs):
    print(args)
    print(kwargs)
    pass
may_function(1, 2, 3, a=3)
print('*' * 50)
may_function(1, 2, 3, **{'a': 3, 'b': 4, 'c': 5})
print('*' * 50)

# 先将args包裹起来，作为包裹位置参数传入给函数，然后打印出来,即解包裹位置参数
def print_hello(name, sex):
    print(name, sex)

args = ('Felix', '男')
print_hello(*args)
print('*' * 50)

# 先将kwargs包裹起来，作为包裹关键字参数传入给函数，然后打印出来，即解包裹关键字参数
def print_hello_1(**kwargs):
    print(kwargs)

kwargs = {'name': 'Felix', 'sex': u'男'}
print_hello_1(**kwargs)



