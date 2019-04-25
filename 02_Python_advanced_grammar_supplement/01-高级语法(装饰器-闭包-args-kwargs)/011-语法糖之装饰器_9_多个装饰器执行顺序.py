# 多个装饰器
# 装饰器函数运行顺序：
# 最靠近原始函数的装饰器@deco_1首先运行——然后运行靠近该装饰器的第二个装饰器@deco_2
# 依次启动完所有的装饰器，运行完所有装饰器中的外函数，然后启动主程序，内函数从外层向里层运行
# 注意，如果装饰器中内函数前面没有外函数，还是先运行所有的装饰器，然后运行原始函数，

import time

# 定义第一个装饰函数，函数的参数是一个函数
def deco_1(func):
    # print()是装饰器包裹函数(内部函数)之前的函数，可以称为外函数
    print("001第一个装饰器开始装饰(最靠近原始函数，最先运行)：")
    # 定义一个内部函数，实现具体的功能，
    # 原始函数带有不定参数，该处传入不定参数到该内部函数
    def wrapper(*args, **kwargs):
        print("第一个装饰器包裹函数(内函数)运行开始")
        return " ( " + func() + " ) "
    # 装饰函数的返回值是内部函数的执行结果
    return wrapper

# 定义第二个装饰器
def deco_2(func):
    print("002第二个装饰器开始装饰(第二个装饰器紧跟着第一个装饰器之后运行)：")
    # 定义一个内部函数，实现具体的功能，
    # 原始函数带有不定参数，该处传入不定参数到该内部函数
    def wrapper(*args, **kwargs):
        print("第二个装饰器包裹函数(内函数)运行开始")
        return " [ " + func() + " ] "
    # 装饰函数的返回值是内部函数的执行结果
    return wrapper

def deco_3(func):
    print("003第三个装饰器开始装饰(第三个装饰器紧跟着第二个装饰器之后运行)：")
    def wrapper(*args, **kwargs):
        print("第三个装饰器包裹函数(内函数)运行开始")
        return " { " + func() + " } "
    # 装饰函数的返回值是内部函数的执行结果
    return wrapper

# 使用@符号拓展函数功能，func_a就具有了deco函数的功能
@deco_3
@deco_2
@deco_1
def func_a():
    print("004原始函数开始运行")
    print("函数返回值装饰之后的效果(由deco1开始装饰)：")
    return "Hello World"


if __name__ == '__main__':
    ret = func_a()
    print(ret)