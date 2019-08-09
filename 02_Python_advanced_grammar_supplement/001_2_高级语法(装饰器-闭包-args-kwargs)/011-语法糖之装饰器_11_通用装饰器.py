# 介绍了这么多，在实际应用中，如果针对每个类别的函数都要写一个装饰器的话，
# 估计就累死了，那么有没有通用万能装饰器呢，答案肯定是有的，直接上代码

# 定义一个通用装饰器，参数采用不定参数args和kwargs
# 返回函数返回值的通用装饰器，装饰器最后返回原始函数的的返回值
def w_test(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return inner

@w_test
def test():
    print('test called')

@w_test
def test1():
    print('test1 called')
    return 'python'

@w_test
def test2(a):
    print('test2 called and value is %d ' % a)
    return a

test()
print("-------------")
ret = test1()
print(ret)

print("-------------")
ret = test2(9)
print(ret)

# 上面test1函数，inner中的func执行后的返回的值给ret，inner又返回了ret，最后又返回了inner
# ret最后就等于test1()运行结束后的返回值
# 参考前面的011-语法糖之装饰器_10_带有返回值的函数进行装饰.py
