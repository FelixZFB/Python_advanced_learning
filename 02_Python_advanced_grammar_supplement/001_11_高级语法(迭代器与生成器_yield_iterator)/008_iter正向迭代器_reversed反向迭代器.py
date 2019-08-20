# -*- coding:utf-8 -*-

# 正向反向生成一系列浮点数，使用迭代器生成
class FloatRange():

    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    # 正向迭代器
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    # 反向迭代器
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

# 创建一个类实例
f = FloatRange(1.0, 4.0, 0.5)

# 生成正向数列,使用for循环调用生成器
f.__iter__() # 直接调用方法不会执行
print("*" * 50)

for x in f.__iter__():
    print(x)
print("*" * 50)

# 生成反向数列
for x in f.__reversed__():
    print(x)
print("*" * 50)

# 上面正向和方向可以直接写成以下形式：
for x in f:
    print(x)
print("*" * 50)

for x in reversed(f):
    print(x)
print("*" * 50)