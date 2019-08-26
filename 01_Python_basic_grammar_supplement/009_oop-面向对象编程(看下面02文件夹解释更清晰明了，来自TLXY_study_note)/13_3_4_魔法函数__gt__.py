# __gt__实例
class Student():

    def __init__(self, name):
        self.name = name

    def __gt__(self, other):
        print("哈哈，{0}会比{1}大吗？".format(self, other))
        print(self.name)
        print(other.name)
        return self.name > other.name

stu1 = Student("one")
stu2 = Student("two")

print(stu1 > stu2)
