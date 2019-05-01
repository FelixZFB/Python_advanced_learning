# 魔法属性，前后双下划线
# __module__表示当前的操作在那个模块
# __class__表示当前操作的是那各类
# __init__初始化方法，类实例化时，该方法自动执行

class Person(object):

    """__doc__用于查看类的描述信息"""

    def __init__(self, name, age):
        print("初始化方法创建类对象时自动执行")
        self.name = name
        self.__age = age

a = Person('Felix', 18)

# 查看类的所有属性
print(Person.__dict__)

print("当前操作的模块：" + a.__module__) # __module__表示当前的操作在那个模块
print(a.__class__)  # __class__表示当前操作的是那各类
print(a.__doc__) # 查看类的描述信息