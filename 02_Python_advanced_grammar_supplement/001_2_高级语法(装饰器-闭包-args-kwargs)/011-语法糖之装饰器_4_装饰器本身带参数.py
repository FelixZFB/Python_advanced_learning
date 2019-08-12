# -*- coding:utf-8 -*-


def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("-----权限级别1-----")
            elif level_num == 2:
                print("-----权限级别2-----")
            return func()
        return call_func
    return set_func

@set_level(1)
def test1():
    print("-----test1-----")
    return "OK"

@set_level(2)
def test2():
    print("-----test2-----")
    return "OK"

test1()
print('*' * 50)
test2()

# 装饰器自己带参数的执行步骤：
# 1. 参数传入到装饰器函数中，运行
# 2. 函数的运行返回值作为装饰器来装饰原始函数，执行步骤和普通装饰器一样，就是多了第一步用于传递参数

# 上面装饰器和前面装饰器相比，就是多了最外层的函数，用来接收装饰器自己的参数
# set_level的返回值是set_func,原始函数指向的地址还是set_func.call_func
# 所以，最新执行时，根据传入的参数判断级别，打印出权限，最后return func()，相当于执行原始函数
