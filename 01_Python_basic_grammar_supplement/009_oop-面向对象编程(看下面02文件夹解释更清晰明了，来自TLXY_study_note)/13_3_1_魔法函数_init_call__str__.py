# 7. 类的常用魔术函数

class A():
    def __init__(self):
        print("我是init哈哈哈哈，我被调用了")

    def __call__(self):
        print("我是call哈哈，我又被调用了一次")

    def __str__(self):
        return "我是str哈哈，我又被调用了字符串函数"

# __init__ 就是一个魔法函数，自动调用
a = A()

# 实例当函数使用，自动调用__call__函数
a()

# str,返回字符串函数
print(a)
