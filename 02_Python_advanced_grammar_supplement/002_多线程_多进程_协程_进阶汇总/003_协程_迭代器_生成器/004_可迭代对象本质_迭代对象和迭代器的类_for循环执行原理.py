# -*- coding:utf-8 -*-

from collections import Iterable, Iterator
import time


# 创建一个可迭代对象的类（可迭代对象包含__iter__方法）
class MyList(object):
    def __init__(self):
        self.container = []
    def add(self, item):
        self.container.append(item)
    def __iter__(self):
        '''__iter__函数返回一个迭代器'''
        return MyIterator()

# 创建一个迭代器的类（迭代器包含__iter__和__next__方法）
class MyIterator(object):
    def __iter__(self):
        pass
    def __next__(self):
        return 111

# 实例化一个对象
mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)

time.sleep(3)
print('判断mylist实例对象是否是可迭代对象', isinstance(mylist, Iterable))

# for循环访问，for循环本质是调用执行了可迭代对象的__iter__方法
for i in mylist:
    print(i)

# 现在运行for循环结果，不断循环的打印出：111
# 上面结果都是返回的__next__函数的返回值，我们要打印出我们自己添加的数字，参考005案例-升级版
# for循环执行步骤：
# 1. 判断mylist是否是一个可迭代对象。(mylist里面实现了__iter__方法，是可迭代对象)
# 2. 第1步成立的情况下，调用__iter__方法，得到__iter__方法的返回值。
# 3. __iter__方法的返回值是一个迭代器对象。（MyIterator()就是一个迭代器对象，包含了__iter__和__next__方法）
# 4. for循环会自动不断的调用迭代器对象中的__next__方法，得到该方法的返回值
# 5. 因此最后，i的打印结果就是111，并且会不断打印下去，因为__next__方法一直有返回值111


# 对比参考：001_11_迭代器与生成器(yield_iterator)文件夹中的001案例
