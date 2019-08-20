# -*- coding:utf-8 -*-

from collections import Iterable, Iterator
import time


# 创建一个可迭代对象的类（可迭代对象包含__iter__方法）
class MyList(object):
    '''自定义一个可迭代对象'''
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        '''__iter__函数返回一个迭代器'''
        myiterator = MyIterator(self)
        return myiterator


# 创建一个迭代器的类（迭代器包含__iter__和__next__方法）
class MyIterator(object):
    '''自定义一个供上面可迭代对象使用的迭代器'''
    def __init__(self, mylist):
        self.mylist = mylist
        # current记录当前访问到的位置
        self.current = 0

    def __next__(self):
        # 当列表的值没有取完时，就会一直取出作为返回值
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        # 返回自己本身
        return self

if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    time.sleep(3)
    for num in mylist:
        print(num)

# for item in Iterable 循环的本质就是先通过iter()函数获取可迭代对象Iterable的迭代器，
# 然后对获取到的迭代器不断调用next()方法来获取下一个值并将其赋值给item，当遇到StopIteration的异常后循环结束

