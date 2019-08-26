# 构造函数__init__

class Dog():
    def __init__(self):
        print("hello")

dog = Dog()
print(type("super"))
print(type(super))


# 多继承和单继承

class Fish():
    def __init__(self, name):
        self.name = name

    def swim(self):
        print("i am swimming ......")

class Bird():
    def __init__(self, name):
        self,name = name

    def fly(self):
        print("i am flying ......")

class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("i am working ......")

# 多继承,不推荐使用
class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name

s = SuperMan("Felix")
s.fly()
s.swim()
s.work()










