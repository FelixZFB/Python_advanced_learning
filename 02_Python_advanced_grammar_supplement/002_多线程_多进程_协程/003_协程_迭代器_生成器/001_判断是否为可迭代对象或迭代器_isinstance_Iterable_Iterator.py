# -*- coding:utf-8 -*-

import time
from collections import Iterable, Iterator

A = 'abc'
B = ['1', '2', '3']
C = {'a':1, 'b':2, 'c':3}
D = 100

time.sleep(3) # 导入语句会出现一个警告，等待一会执行后面的语句

# 判断上面各种类型是否是可迭代对象
print(isinstance(A, Iterable))
print(isinstance(B, Iterable))
print(isinstance(C, Iterable))
print(isinstance(D, Iterable)) # int类型不是可迭代对象，因此不能使用for i in 100:这种语法
print('*' * 50)


# 将可迭代对象转换为迭代器
E = iter(A)
F = iter(C)
print(isinstance(E, Iterator))
print(isinstance(F, Iterator))
print('*' * 50)