# -*- coding:utf-8 -*-

# type可以接受一个类的描述作为参数，然后返回一个类
# type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

# 常规创建类
class Test():
    name = 100
    pass

t1 = Test()
print(Test)
print(t1)
print('*' * 50)


# 使用type创建一个类对象和实例对象
# 等号的左边变量名和括号里面的类名保持一致，可以不一样，单最好保持一致防止使用时出错
Test1 = type('Test1', (), {'name': 100})
t2 = Test1()
print(Test1)
print(t2)
print('*' * 50)

# 使用help函数查看两个类是否一致
print(help(Test))
print('*' * 50)
print(help(Test1))
print('*' * 50)
# 结果显示两个类的描述是一致的

# type就是一个元类
# 使用关键字class时Python在幕后做的事情，就是通过元类type来实现的。
