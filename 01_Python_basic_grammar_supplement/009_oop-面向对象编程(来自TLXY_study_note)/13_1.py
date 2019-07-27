
# 访问公有变量和私有变量的方法

'''定义一个学生的类'''
class Person():
    # 公有成员
    name = "liuying"
    age = 20
    # 私有成员
    __age = 20

p = Person()
# 访问公有变量
print(p.name)
# 访问私有变量
# print(p.__age)
# 访问私有变量的方法
# 采用字典查看age对应的变量名称为：_Person__age
print(Person.__dict__)
print(p._Person__age)


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


# Mixin设计模式案例
# 原始写法
class Person():
    name = "Felix"
    age = 18

    def eat(self):
        print("Eat...")

    def drink(self):
        print("Drink...")

    def sleep(self):
        print("Sleep...")

class Teacher(Person):
    def work(self):
        print("Work...")

class Student(Person):
    def study(self):
        print("Study...")

# 助教是学生中选取，具有老师的功能，也有学习的功能
class Tutor(Teacher, Student):
    pass

t = Tutor()

print(Tutor.__mro__)

# Mixin设计模式代码写法
class Person():
    name = "Felix"
    age = 18

    def eat(self):
        print("Eat...")

    def drink(self):
        print("Drink...")

    def sleep(self):
        print("Sleep...")

class TeacherMixin():
    def work(self):
        print("Work...")

class StudentMixin():
    def study(self):
        print("Study...")

# 老师只有功能，没有继承Person类
class TutorM(Person, TeacherMixin, StudentMixin):
    pass

t = TutorM()

print(TutorM.__mro__)

# 查看MRO解析顺序已经变化了


# 类中的相关函数
class A():
    name = "NoName"

class B(A):
    pass

a = A()
print(issubclass(B, A))
print(isinstance(a, A))
print(isinstance(a, B))
print(hasattr(a, "name"))
print(dir(a))








