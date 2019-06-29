# -*- coding:utf-8 -*-


# yield生成器其实是一种特殊的迭代器，不过这种迭代器更加优雅。
# 它不需要像迭代器对象一样写__iter__()和__next__()方法了，
# 只需要一个yiled关键字。 生成器一定是迭代器（反之不成立），
# 因此任何生成器也是以一种懒加载的模式生成值。
# 生成器特殊的地方在于函数体中没有return关键字，函数的返回值是一个生成器对象。


# 生成器表达式(generator expression)
# 生成器表达式是列表推倒式的生成器版本，看起来像列表推导式，
# 但是它返回的是一个生成器对象而不是列表对象。

# 迭代器对象，使用next或者for循环访问
a = (x for x in range(10))
print(a)
print(type(a))
print("*" * 100)

# 列表对象
a = [x for x in range(10)]
print(a)
print(type(a))
print("*" * 100)


# 定义一个生成器函数，包含yield的函数就是生成器函数
def f():

    print('f(), 1')
    yield 1

    print('f(), 2')
    yield 2

    print('f(), 3')
    yield 3

# 函数包含生成器，调用时候并不会执行内部语句
f()
g = f()
# 使用next执行生成器函数，每次执行到yield语句时候中止，
# 然后等待继续调用
print(next(g))
print("*" * 100)
print(next(g))
print("*" * 100)
print(next(g))
print("*" * 100)

# g就是一个迭代器，返回的就是g本身
print(g.__iter__())
print(g.__iter__() is g)