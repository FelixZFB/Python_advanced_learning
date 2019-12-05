# 魔法属性，前后双下划线
# __module__表示当前的操作在那个模块
# __class__表示当前操作的是那个类
# __init__初始化方法，类实例化时，该方法自动执行
# __doc__类的描述和说明文档信息
# __dict__查看类所有属性(所有方法),也可以查看模块的所有属性方法，查看类实例对象的所有属性

class Person(object):

    """__doc__用于查看类的描述信息。我是一个person的类"""

    def __init__(self, name, age):
        print("初始化方法创建类对象时自动执行")
        self.name = name
        self.__age = age

a = Person('Felix', 18)

# 查看类所有属性(所有方法),也可以查看模块的所有属性方法，查看类实例对象的所有属性
print(Person.__dict__) # 查看类的属性和方法
print('*' * 50)

print("当前操作的模块：" + a.__module__) # __module__表示当前的操作在那个模块
print('*' * 50)
print(a.__class__)  # __class__表示当前操作的是那个类
print('*' * 50)
print(a.__doc__) # 查看类实例对象的描述信息,类定义时候进行了描述
print('*' * 50)
print(a.__dict__) # 查看类实例对象的属性