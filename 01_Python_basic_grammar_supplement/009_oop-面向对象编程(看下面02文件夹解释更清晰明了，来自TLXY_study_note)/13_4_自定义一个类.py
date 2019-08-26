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






