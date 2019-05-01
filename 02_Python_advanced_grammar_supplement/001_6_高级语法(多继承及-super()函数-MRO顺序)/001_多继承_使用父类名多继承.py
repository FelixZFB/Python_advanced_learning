# coding=utf-8

# 下面为方式1的案例：
# 输出结果可以发现，该爷爷类有两个子类，孙子类（继承了两个子类）执行的时候
# 爷爷类Parent的初始化方法会被调用两次，如果有多个子类，爷爷类会调用很多次
# 这样会占用大量的资源，此外python默认只打开1024个文件
# 大型程序中，这种继承方法，会占用大量资源，打开大量相同的文件
# 我们希望的结果是只调用一次即可

# 只有属性name
class Parent(object):
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')

# 新建属性age,继承属性name
class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        # 继承父类中的__init__初始化方法
        Parent.__init__(self, name)
        print('Son1的init结束被调用')

# 新建属性gender,继承属性name
class Son2(Parent):
    def __init__(self, name, gender):
        print('Son2的init开始被调用')
        self.gender = gender
        # 继承父类中的__init__初始化方法
        Parent.__init__(self, name)
        print('Son2的init结束被调用')

# 继承属性name，age，gender
class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        # 继承父类的初始化方法
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print('Grandson的init结束被调用')

# 创建一个实例对象，初始化方法__init__会自动调用
print("方式1多继承执行顺序：由最底层向上层依次执行所有的继承")
gs = Grandson('grandson', 12, '男')

print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)

print("******多继承使用类名.__init__ 发生的状态******\n\n")