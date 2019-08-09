# -*- coding: utf-8 -*-

# python装饰器就是用于拓展原来函数功能的一种函数

# 装饰器函数的特别之处：
# 1.参数是一个函数（函数的参数是一个函数）；
# 2.返回值是一个函数（内部定义一个函数，返回值就是返回这个函数）
# 装饰器好处：使用python装饰器的可以在不用更改原函数的代码前提下给函数增加新的功能

# 1. 看一个例子，定义一个函数a
# 2. 我们需要获取函数a的运行时间
# 3. 方法1：篡改原函数a，参照篡改后的函数b
# 4. 方法2：不篡改原函数a, 定义一个新函数c，函数a作为参数传入，参照函数c

import time

# 原始函数
def func_a():
    print("hello")
    time.sleep(1)
    print("world")

# 方法1：直接修改函数增加获取函数运行时间的功能
def func_b():
    startTime = time.time()

    print("hello")
    time.sleep(1)
    print("world")

    endTime = time.time()
    msecs = (endTime - startTime)*1000
    print("函数func_a运行耗时：%d ms" %msecs)

func_b()
print()


# 方法2：定义一个新函数func_c，函数func_a作为参数传入
def func_c(func_a):
    startTime = time.time()
    func_a()
    endTime = time.time()
    msecs = (endTime - startTime) * 1000
    print("函数func_a运行耗时：%d ms" % msecs)

# 运行上面的func_c函数，将func_a作为参数传入
if __name__ == '__main__':
    # 将原始函数func_a作为参数传入到func_c函数中
    f = func_a
    func_c(f)
    # 函数f的名称就是func_a
    print("f.__name__is:", f.__name__)

# 函数c可以实现获取运行时间的功能
# 但是如果有1000个func_a函数，则需要把func_a函数传入到func_c函数1000次
# 然后运行func_c函数1000次
# 是不是非常耗时和耗电呢？
# 看011-语法糖之装饰器_2.py



