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
print('*' * 50)


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
# 然后接着name作为实参传递给name,value作为形参传递形参传递给value,然后不断循环进入死循环
p.age = 20