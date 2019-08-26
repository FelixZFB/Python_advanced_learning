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