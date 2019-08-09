# 位置参数，默认参数，可变参数的混合使用
# 基本原则是：先位置参数，默认参数，包裹位置，包裹关键字(定义和调用都应遵循)

# 参数使用原则
def func(name, age, *args, **kargs):
    print(name, age, args, kargs)

# 先默认传入位置参数name和age，然后再传入包裹位置，最后传入包裹关键字
func('Felix', 25, 'music', 'sport', grade=2)
print()

# *args与位置参数和默认参数混用
# *args要放到位置参数后面，默认参数要放最后(键值类型放最后)
# y=1是默认参数，如果传入新的值，就用新的值替换默认的1
def foo(x, *args, y=1):
    print(x)
    print(y)
    print(*args)
foo(1, 2, 3, 4, 5, y=10000)

# 下面加*是一个整体，元组
def foo(x, *args, y=1):
    print(x)
    print(y)
    print(args)
foo(1, 2, 3, 4, 5, y=10000)


