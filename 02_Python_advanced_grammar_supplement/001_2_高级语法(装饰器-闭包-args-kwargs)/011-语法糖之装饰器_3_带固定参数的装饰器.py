# 带有固定参数的装饰器函数
# 011-语法糖之装饰器_2.py中函数中加入参数

import time

# 定义一个装饰函数，函数的参数是一个函数
def deco(func):
    # 定义一个内部函数，实现具体的功能，
    # 原始函数带有参数，该处传入参数到该内部函数
    def wrapper(a, b):
        startTime = time.time()
        func(a, b)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("原函数获得的拓展功能，原始函数func_a运行耗时：%d ms" % msecs)
    # 装饰函数的返回值是内部函数的执行结果
    return wrapper

# 使用@符号拓展函数功能，func_a就具有了deco函数的功能
@deco
def func_a(a, b):
    print("带有固定参数的装饰器演示：")
    time.sleep(1)
    print("传入的参数求和：%d" % (a + b))

if __name__ == '__main__':
    func_a(1, 2)
