# func和funb函数参数一样，先向func中传入位置参数和不定参数
# func中调用了funb方法，要向传入到funb中参数和最初传到func中的参数一模一样
# 此时，就需要对func中已经打包的为元组和字典类型的*args, **kwargs参数拆包
# 拆包的方法就是funb中的不定参数前面的*和**写上即可，如果只写一个，就只会拆包一个

def funb(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

def func(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    print()
    print("以下为funb函数执行结果：")
    # 拆包的写法
    funb(name, age, *args, **kwargs)
    # 除了name和age作为位置参数传入，*args进行了拆包，后面关键字参数以字典作为一个不定位置参数
    print()
    funb(name, age, *args, kwargs)
    print()
    # 只对关键字参数拆包了，前面未解包的当成一个元组参数传入了
    funb(name, age, args, **kwargs)
    # 除了name和age作为位置参数传入，后面的都当做不定位置参数
    print()
    funb(name, age, args, kwargs)


# 先默认传入位置参数name和age，然后再传入包裹位置，最后传入包裹关键字
func('Felix', 25, 'music', 'sport', grade=2)