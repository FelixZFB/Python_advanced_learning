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

# __mro__查看类的继承顺序
print(TutorM.__mro__)

# 查看MRO解析顺序已经变化了