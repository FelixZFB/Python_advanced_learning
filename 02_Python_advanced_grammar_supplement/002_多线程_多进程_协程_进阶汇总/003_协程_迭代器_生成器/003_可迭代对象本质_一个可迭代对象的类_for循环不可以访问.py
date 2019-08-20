# -*- coding:utf-8 -*-

from collections import Iterable, Iterator
import time


class MyList(object):
    def __init__(self):
        self.container = []
    def add(self, item):
        self.container.append(item)
    def __iter__(self):
        '''__iter__函数返回一个迭代器'''
        pass


mylist = MyList()

# 调用add方法，向列表中添加元素
mylist.add(1)
mylist.add(2)
mylist.add(3)

time.sleep(3)
print(mylist.container)
print(isinstance(mylist, Iterable))
print(isinstance(mylist, Iterator))

# for循环访问，for循环本质是调用执行了可迭代对象的__iter__方法
for i in mylist:
    print(i)

# 上面判断已经是一个可迭代对象了，但是还是不能for循环访问，但是错误提示已经变了
# 运行结果
# TypeError: iter() returned non-iterator of type 'NoneType'



