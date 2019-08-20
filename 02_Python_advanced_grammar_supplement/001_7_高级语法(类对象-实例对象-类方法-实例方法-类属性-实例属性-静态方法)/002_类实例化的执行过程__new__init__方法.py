# 类实例化代码的执行过程，比如：obj1 = Province('山东省')

# 创建一个类对象
class Province():
    # 类属性，所有实例省份都属于中国，共有的属性
    country = '中国'
    # 初始化属性，用来接收实例中的参数
    def __init__(self, name):
        # 实例属性，实例特有，每个实例的name不相同
        self.name = name

# 创建第一个实例对象
obj1 = Province('山东省')
# 直接访问实例属性
print(obj1.name)


# obj1 = Province('山东省')该代码执行过程
# 1. 上面创建了一个类对象，已经有了一个内存空间
# 2. 实例化第一步执行类中的：__new__函数(该函数默认不用写）
# __new__函数的作用就是创建一个实例对象，给它分配一个内存空间
# 3. 接下来调用__init__函数，里面的self指向刚刚创建的实例对象
# (类对象内部的self指向obj1，self.name=name=obj1.name)
# name参数就接收传递进来的山东省

# 如果类中方法调用类中的其它对象属性，调用时候加上self即可