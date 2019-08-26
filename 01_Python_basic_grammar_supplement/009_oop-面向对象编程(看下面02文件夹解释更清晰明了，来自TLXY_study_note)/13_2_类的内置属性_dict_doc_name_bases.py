# 6.7. 类的属性
# 类的属性案例
# 增加一个统一name的方法
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.setName(name)

    # 介绍自己
    def intro(self):
        print("Hi, my name is {0}".format(self.name))

    def setName(self, name):
        self.name = name.upper()

s1 = Student("Felix", 20)
s1.intro()

# peroperty案例
# 对于任意输入的姓名都以大写方式保存
# 年龄，希望内部统一用整数保存
# property(fget, fset, fdel, doc)

class Person():
    '''一个人的类'''
    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self.name = "NoName"

    name = property(fget, fset, fdel, "对name进行操作")

p1 = Person()
# 调用name, 然后调用property中的fset函数，将felix作为实参传入，并将名称全部大写
p1.name = "felix"
# 调用name, 然后调用property中的fget函数，将name的赋值乘以2，字符串乘以2，就是打出来两个
print(p1.name)


# 获取类的内置属性
print(p1.__dict__)
print(Person.__dict__) # 以字典的方式显示成员的组成
print(Person.__doc__) # 获取类的说明文档
print(Person.__name__) # 获取类的名称
print(Person.__bases__) # 获取类的父类





