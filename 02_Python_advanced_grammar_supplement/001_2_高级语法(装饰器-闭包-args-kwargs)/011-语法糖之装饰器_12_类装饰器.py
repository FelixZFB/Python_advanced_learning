# 装饰器函数其实是一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。
# 在python中，一般callable对象都是函数，但是也有例外。
# 比如只要某个对象重写了call方法，那么这个对象就是callable的。

class Test(object):
    def __call__(self, *args, **kwargs):
        print('call called')

t = Test()
print(type(t))
print(t())

# 使用类装饰函数
class Test(object):

    def __init__(self, func):
        print('test init')
        print('func name is %s ' % func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('装饰器中的功能')
        self.__func()


@Test
def test():
    print('this is test func')

test()

# 和之前的原理一样，当python解释器执行到到@Test时，
# 会把当前test函数作为参数传入Test对象，首先调用init方法，
# 同时将test函数指向创建的Test对象，那么在接下来执行test()的时候，
# 其实就是直接对创建的对象进行调用，执行其call方法