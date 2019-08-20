# 实例方法、类方法和静态方法，三种方法在内存中都归属于类，区别在于传入的参数和调用方式不同:
# 传入的参数分别是：self(实例化对象),cls(类本身)，无参数

# 实例方法：由对象调用；至少一个self参数；执行实例方法时，自动将调用该方法的实例化对象赋值给self；
# 实例化方法中可以修改实例的属性

# 类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类赋值给cls；
# 类方法中可以修改类的属性

# 静态方法：由类调用；无默认参数；内部使用；
# 静态方法特殊：静态方法不需要传入实例或者类，它是用来被类内部普通方法或类方法使用的一种方法


class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义实例方法，至少有一个self参数，self指向实例化的对象 """
        print('实例方法')
        # 类调用自己的静态方法
        print("类调用自己的静态方法")
        self.static_func()

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数，cls指向类对象 """
        print('类方法')

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""
        print('静态方法')

# 创建一个实例
f = Foo("中国")

print("实例对象可以调用实例方法，类方法，静态方法：")
# 调用实例方法，类方法，静态方法
f.ord_func()
f.class_func()
f.static_func()

print("\n类只能调用类方法和静态方法:")
# 调用类方法
Foo.class_func()
# 调用静态方法
Foo.static_func()

# Foo.ord_func()
# 因为实例方法必须传入self参数，self参数是一个实例化对象
