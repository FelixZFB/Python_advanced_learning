# 11. 自定义类的实例

# 函数名称可以直接作为变量名使用
def sayHello(name):
    print("{0}, 你好! 来一发?".format(name))


sayHello("Felix")


# 自己组装一个类

class A():
    pass


def say(self):
    print("saying...")


# A类和say函数组装成B类

class B():

    def say(self):
        print("saying...")


# 直接调用函数say
say(111)

# A作为一个类，将say函数赋值给A.say函数，A.say就相当于A类下的一个方法say,该方法就调用的是say函数
A.say = say
a = A()
a.say()

b = B()
b.say()


# 利用type造一个类

# 先定义类应该具有的成员函数
def say(self):
    print("saying...")

def talk(self):
    print("talking...")

# 用type来创建一个类
C = type("AName", (object, ), {"class_say": say, "class_talk": talk})


# 使用上面创建的类

c = C()
dir(c)



# 元类演示

# 元类的写法是固定的，必须继承子type
# 元类命名以MetaClass结尾
class TulingMetaClass(type):

    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        # 自己业务受理
        print("我是元类")
        return type.__new__(cls, name, bases, attrs)

# 元素定义完就可以使用元类
class Teacher(object, metaclass=TulingMetaClass):
    pass

t = Teacher()


