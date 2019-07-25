# -*- coding:utf-8 -*-

import time

# 包含yield关键字，就变成了生成器函数
# 调用函数并不会执行语句


def foo():
    print('Starting.....')
    while True:
        res = yield 4
        print("res:", res)
        time.sleep(3)


# 下面调用foo时，并不是调用执行函数，而是创建了一个生成器对象
g = foo()
print(g)
print(type(g))
print("*" * 100)

# 使用for循环访问生成器对象
# for循环会自动调用next函数，直到没有值访问
# 通过查看和003_1执行结果一样
for i in g:
    print(i)

# 执行步骤起始和003_1一样，也是每次执行到yield后面的值4停止
# 每循环一次然后，从yield中断处开始