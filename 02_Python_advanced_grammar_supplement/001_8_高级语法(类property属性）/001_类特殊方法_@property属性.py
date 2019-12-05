# 类特殊方法，property属性
# 定义property属性共有两种方式，分别是【装饰器】和【类属性】，而【装饰器】方式针对经典类和新式类又有所不同。
# 通过使用property属性，能够简化调用者在获取数据的流程

# property属性具体实现方式：
# 第一种：使用类方法前面加上@property，参考案例001和002
# 第二种: @property、@方法名.setter、@方法名.deleter修饰的方，实现获取、修改、删除属性,参考案例003
# 第三种: 类里面创建property对象，传入四个参数，实现获取、修改、删除属性和属性的说明文档，参考案例004和005

# property属性目的就是为了优化代码，简化代码

# 比如以下案例: 调用该方法可以获得一个属性，调用该方法写法和调用属性一样

class Goods():

    def __init__(self, name):
        self.name = name

    # 定义一个属性的特殊方法,并且参数只有一个self，有一个返回值
    @property
    def size(self):
        return 100

# 实例化对象
obj = Goods("Felix")
# 调用实例属性
name = obj.name
print(name)

# 调用property属性，方法后面的括号不能写
# 这样就类似于调用实例中的一个属性
ret = obj.size # 直接就是返回值
print(ret)