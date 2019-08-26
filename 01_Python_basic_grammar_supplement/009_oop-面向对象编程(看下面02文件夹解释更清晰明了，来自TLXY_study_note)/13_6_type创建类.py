# 利用type造一个类

# 先定义类应该具有的成员函数
def say(self):
    print("saying...")

def talk(self):
    print("talking...")

# 用type来创建一个类
# 传入类名，继承的父类，类有的方法字典
AName = type("AName", (object, ), {"class_say": say, "class_talk": talk})


# 使用上面创建的类

c = AName()
c.class_say()
c.class_talk()
print(dir(c))

