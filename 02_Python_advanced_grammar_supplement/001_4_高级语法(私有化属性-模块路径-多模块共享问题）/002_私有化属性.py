#coding=utf-8

class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age # 私有化属性，使用 from xxx import * 不会被导入，类对象和子类可以访问
        self.__taste = taste # 私有化属性，外界无法直接访问

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self): # 普通方法
        self._work()
        self.__away()

    def _work(self): # 普通方法
        print('my _work')

    def __away(self): # 私有化方法
        print('my __away')

class Student(Person):
    def construction(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def testbug():
        _Bug.showbug()


class _Bug(object):
    @staticmethod
    def showbug():
        print("showbug")

# 私有化属性模块内可以访问，
# 但是，当from  cur_module import *时，不导入_单下划线私有属性
# 但是，创建的类对象和子类可以访问

s1 = Student('jack', 25, 'football')
s1.showperson()
print('*'*20)