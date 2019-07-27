# 7. 类的常用魔术函数

class A():
    def __init__(self):
        print("哈哈哈哈，我被调用了")

    def __call__(self):
        print("哈哈，我又被调用了一次")

    def __str__(self):
        return "哈哈，我又被调用了字符串函数"

# __init__ 就是一个魔法函数，自动调用
a = A()

# 实例当函数使用，自动调用__call__函数
a()

# 返回字符串函数
print(a)


# __str__ 和 __repr__的区别

class A():

    def __str__(self):
        return "__str__"

a = A()
print(a)

class A():

    def __repr__(self):
        return "__repr__"

a = A()
print(a)


# str和repr同时存在时候，返回字符串执行的是str函数
class A():

    def __str__(self):
        return "__str__"

    def __repr__(self):
        return "__repr__"

a = A()
print(a)

# str和repr本质区别，查看官方文档实例

import datetime

today = datetime.date.today()

# str返回的字符串可读性更强
print(str(today))

# repr返回结果应更准确。存在的目的在于调试，便于开发者使用。
# 细心的读者会发现将 __repr__ 返回的方式直接复制到命令行上，是可以直接执行的。
print(repr(today))


# __getattr__魔法函数

class A():

    name = "Felix"
    age = 18

    def __getattr__(self, item):
        print("不存在这个属性")
        print(item)

a = A()
print(a.name)
print(a.sex)


# __setattr__魔法函数实例
class Person():

    name = "Felix"
    age = 18

    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print("设置属性：{0}".format(name))
        # 下面的语句会导致不停的设置，进入死循环
        # self.name = value
        # 上述代码会进入死循环，避免这种情况采用以下方法，调用父类的魔法函数
        super().__setattr__(name, value)


p = Person()
print(p.__dict__)
# 进行赋值时候调用__setattr__函数，age作为实参传递给形参name,20作为实参传递给形参value
# 第一次运行结果就是：设置属性：age
# 然后接着运行96行代码name作为实参传递给name,value作为形参传递形参传递给value,然后不断循环进入死循环
p.age = 20


# __gt__实例
class Student():

    def __init__(self, name):
        self.name = name

    def __gt__(self, other):
        print("哈哈，{0}会比{1}大吗？".format(self, other))
        print(self.name)
        print(other.name)
        return self.name > other.name

stu1 = Student("one")
stu2 = Student("two")

print(stu1 > stu2)


# 类和对象的三种方法
class Person():

    # 实例方法
    def eat(self):
        # 打印对象自己
        print(self)
        print("eating...")

    # 类方法
    # 类方法的第一个参数，命名为cls,区别于实例方法的self
    @classmethod
    def play(cls):
        print(cls)
        print("playing...")

    # 静态方法
    # 不需要第一个参数表示自身或者类
    @staticmethod
    def say():
        print("saying...")

Felix = Person()
# 调用实例方法
Felix.eat()
# 调用类方法
Person.play()
# 输出结果，实例方法里面有个对象object，并指出所在的位置，类方法里面没有
# <__main__.Person object at 0x0000029C04D88D30>
# eating...
# <class '__main__.Person'>
# playing...
Felix.play()
# 调用静态方法
Felix.say()


# 类属性property
class A():

    def __init__(self):
        self.name = "Felix"
        self.age = 18

    # 此功能，对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print("我被读取了")
        return self.name

    # 模拟的是对变量进行写操作的时候执行的功能
    def fset(self):
        print("我被写入了")
        self.name = "Fangbai" + name

    # fdel模拟的是删除变量时候进行的操作
    def fdel(self):
        pass

    # 第一个参数代表读取时候需要调用的函数
    # 第二个参数代表写入时候需要调用的函数
    # 第三个是删除
    # 第四个是说明文档
    name2 = property(fget, fset, fdel, "这是property的一个实例")

a = A()
print(a.name)
print(a.name2)

# 抽象类的实现
import abc

# 声明一个类并且指定当前类的元素
class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    # 定义具体的方法
    def sleep(self):
        print("sleeping...")


