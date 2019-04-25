# 对带返回值的函数进行装饰

def w_test(func):
    def inner():
        print('w_test inner called start')
        func()
        print('w_test inner called end')
    return inner


@w_test
def test():
    print('this is test fun')
    return 'hello'

ret = test()
print(ret)

# test进行装饰后指向inner函数，首先打印出：w_test inner called start
# 接着执行func()，此时才是执行的原始函数test()，打印出：this is test fun
# 原始函数test()虽然有返回值字符串hello，但是inner内部没有变量接受，再将其返回
# 接着执行inner最后一句，打印出：w_test inner called end
# 最后打印出ret value is None，装饰后的test()函数运行结束

# 在inner函数中对test进行了调用，但是没有接受返回值，也没有进行返回，那么默认就是None了

# 希望最后test()运行结束后返回字符串hello
# inner函数内接受func的返回值，inner函数最后返回该接受值

print("\n修改后的代码：")
def w_test(func):
    def inner():
        print('w_test inner called start')
        str = func()
        print('w_test inner called end')
        return str
    return inner


@w_test
def test():
    print('this is test fun')
    return 'hello'

ret = test()
print(ret)


