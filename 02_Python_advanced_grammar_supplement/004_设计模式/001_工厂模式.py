# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/9 12:21
Desc:
'''
# 工厂模式是一个在软件开发中用来创建对象的设计模式。
# 当程序运行输入一个“类型”的时候，需要创建于此相应的对象。
# 这就用到了工厂模式。在如此情形中，实现代码基于工厂模式，
# 可以达到可扩展，可维护的代码。
# 当增加一个新的类型，不在需要修改已存在的类，只增加能够产生新类型的子类。

# 使用工厂模式应用场景：
# 不知道用户想要创建什么样的对象


class Car(object):
    def run(self):
        print('so~so~de')

    def stop(self):
        print('ci~~~~')

class BMW(Car):
    pass

class Benz(Car):
    pass

class CarFactory(object):
    def make_car(self, name):
        if name == 'BMW':
            return BMW()
        if name == 'Benz':
            return Benz()

factory = CarFactory()
car = factory.make_car('BMW')
print(type(car))  # <class '__main__.BMW'>