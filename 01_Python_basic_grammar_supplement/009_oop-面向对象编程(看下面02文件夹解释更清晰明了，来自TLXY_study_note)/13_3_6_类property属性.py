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