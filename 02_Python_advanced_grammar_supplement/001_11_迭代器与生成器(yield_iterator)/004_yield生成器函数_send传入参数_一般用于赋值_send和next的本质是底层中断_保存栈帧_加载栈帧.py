# -*- coding:utf-8 -*-

# 接003案例，send传入参数

# 包含yield关键字，就变成了生成器函数
# 调用函数并不会执行语句
def foo():
    print('Starting.....')
    while True:
        res = yield 4
        print("res:", res)

# 下面调用函数并没有执行，可以先将后面的语句注释掉
# 逐行运行代码观察效果
g = foo()
print("第一次调用执行结果：")
print(next(g))
print("*" * 100)

print("第二次调用执行结果(传入参数)：")
print(g.send(7)) # g.send(7)执行结果还是yield后面返回的值4
print("*" * 100)

print("第三次调用执行结果：")
print(next(g))
print("*" * 100)

# send函数的概念：003案例中第二次调用时res的值为什么是None，这个变成了7，到底为什么？
# 这是因为，send是发送一个参数给res的，因为上面讲到，return的时候，并没有把4赋值给res，
# 下次执行的时候只好继续执行赋值操作，只好赋值为None了，而如果用send的话，开始执行的时候，
# 先接着上一次（return 4之后）执行，先把7赋值给了res,然后执行next的作用，
# 遇见下一回的yield，return出结果后结束（return的结果都是4，每次代码最后的结果都是4）。
#
# 1.程序执行g.send(7)，程序会从yield关键字那一行继续向下运行，send会把7这个值赋值给res变量
#
# 2.由于send方法中包含next()方法，所以程序会继续向下运行执行print方法，然后再次进入while循环
#
# 3.程序执行再次遇到yield关键字，yield会返回后面的值后，程序再次暂停，直到再次调用next方法或send方法。

# 深层次补充：(003和004的上面描述只是为了容易理解，描述为暂停和赋值)
# 比如说“send方法中包含next()”send先赋值然后在执行next，
# 从一些代码直观上来讲好像是这样，但其实并不是，
# 第一，其实并不是赋值，第二，底层send和next其实都是调用gen_send_ex(PyGenObject *gen,PyObject *arg,int exc)这个函数，
# 只是第二个参数不一样，send也不一定要带参数，尤其是第一次使用send来启动生成器，send带参数还是不允许的。
# 如果对中断了解的话，其实不要把这个当成return来看，因为根本就不是，应该当成中断来理解，
# 因为底层的实现就是中断的原理，保存栈帧，加载栈帧。