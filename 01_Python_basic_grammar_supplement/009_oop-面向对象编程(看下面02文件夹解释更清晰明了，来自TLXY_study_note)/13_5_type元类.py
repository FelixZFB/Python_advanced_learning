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