# -*- coding:utf-8 -*-

from collections import Iterable

class MyList(object):
    def __init__(self):
        self.container = []
    def add(self, item):
        self.container.append(item)

mylist = MyList()

# 调用add方法，向列表中添加元素
mylist.add(1)
mylist.add(2)
mylist.add(3)

print(mylist.container)
print(type(mylist.container))
print(isinstance(mylist, Iterable))

# mylist初始化属性就有一个列表
# 但是使用for循环并不能访问
for i in mylist:
    print(i)

# 运行结果：
# TypeError: 'MyList' object is not iterable

