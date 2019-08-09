# func和funb函数参数一样，先向func中传入位置参数和不定参数
# func中调用了funb方法，要向传入到funb中参数和最初传到func中的参数一模一样
# 此时，就需要对func中已经打包的为元组和字典类型的*args, **kwargs参数拆包

# 拆包
def funb(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

# 先默认传入位置参数name和age，然后再传入包裹位置，最后传入包裹关键字
# 多个关键字，要使用字典,并且前面加**
funb('Felix', 25, 'music', 'sport', grade=2)
print('*' * 50)
funb('Felix', 25, 'music', 'sport', **{'grade':2, 'class': 3})


print('*' * 50)

# 加*打印一般不用
def func(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(*args)
    print(*kwargs)
func('Felix', 25, 'music', 'sport', grade=2)