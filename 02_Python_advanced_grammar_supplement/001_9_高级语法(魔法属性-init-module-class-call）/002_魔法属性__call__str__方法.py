# __call__方法：实例化对象后面加括号，触发执行。
# 注：__init__方法的执行是由创建对象自动触发的，即：对象 = 类名() ；
# 而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()

class Foo(object):

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("__call__")

    def __str__(self):
        return "获取对象描述时候自动调用"

obj  = Foo() # 自动执行__init__方法
obj() # 执行__call__方法

# __str__获取对象描述时候自动调用，有以下两种方式调用对象描述
# 方式1：直接打印对象，返回__str__的返回值
print(obj)
# 方式2: 使用格式化输出
print("方式2：%s" % obj)