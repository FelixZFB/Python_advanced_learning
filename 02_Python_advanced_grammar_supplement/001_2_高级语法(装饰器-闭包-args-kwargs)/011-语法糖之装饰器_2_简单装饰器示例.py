# 一个简单的装饰器演示
# 用装饰器函数实现前面的功能
# 将上面函数稍加改写

# 装饰器函数的特别之处：
# 1.参数是一个函数（函数的参数是一个函数）；
# 2.返回值是一个函数（内部定义一个函数，返回值就是返回这个函数）

import time

# 定义一个装饰函数，函数的参数是一个函数
def deco(func):
    # 定义一个内部函数，实现具体的功能
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("原函数获得的拓展功能，原始函数func_a运行耗时：%d ms" % msecs)
    # 装饰函数的返回值是内部函数的执行结果
    return wrapper

# deco函数最终的运行结果就是：原函数获得的拓展功能，原始函数func_a运行耗时：xxx ms

# 使用@符号拓展函数功能，func_a就具有了deco函数的功能
@deco
def func_a():
    print("hello")
    time.sleep(2)
    print("world")

if __name__ == '__main__':
    # 将func_a定义为对象f
    f = func_a
    # f() == func_a()
    f()