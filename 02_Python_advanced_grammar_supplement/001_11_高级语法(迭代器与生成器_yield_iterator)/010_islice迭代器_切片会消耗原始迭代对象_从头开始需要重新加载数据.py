# -*- coding:utf-8 -*-
from itertools import islice

l = list(range(1, 21, 1))
print(l)

# 将列表转换为迭代器对象
t = iter(l)

for x in islice(t, 5):
    print(x)
print("*" * 50)

# 原来的迭代对象已经消耗了，再次选取已经从6开始了
for x in islice(t, 0, 5):
    print(x)
