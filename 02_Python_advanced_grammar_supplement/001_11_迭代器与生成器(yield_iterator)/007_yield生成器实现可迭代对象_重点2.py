# -*- coding:utf-8 -*-

# 定义一个生成器函数，包含yield的函数就是生成器函数
def f():

    print('f(), 1')
    yield 1

    print('f(), 2')
    yield 2

    print('f(), 3')
    yield 3

# 函数包含生成器，调用时候并不会执行内部语句
# yield是一个类似return的关键字，只是这个函数返回的是个生成器
# 当你调用这个函数时，函数内部代码并不立即执行，这个函数只是返回一个生成器对象。
# 当你使用for迭代时，函数中的代码才会执行。

f()
g = f()

# 上面的g使用for循环访问
for x in g:
    print(x)
