# -*- coding:utf-8 -*-

# 创建一个类
class ObjectCreator(object):
    pass

# 类作为一个对象，也可以和普通变量一样进行操作
# 打印出类对象
print(ObjectCreator)
print('*' * 50)

# 类对象作为一个变量赋值操作
def echo(o):
    print(o)
echo(ObjectCreator)
print('*' * 50)

# 你可以将类赋值给一个变量
ObjectCreatorMirror = ObjectCreator
print(ObjectCreatorMirror)
print('*' * 50)

# 创建一个实例对象
obj = ObjectCreatorMirror()
print(obj)
print('*' * 50)

# <class '__main__.ObjectCreator'> 类对象
# <__main__.ObjectCreator object at 0x000001DD407576A0> 类实例对象
