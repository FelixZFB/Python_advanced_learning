# 类中的相关函数
class A():
    name = "NoName"

class B(A):
    pass

a = A()


# B是否是A的子类
print(issubclass(B, A))

# 检测一个对象是否为一个类的实例
print(isinstance(a, A))
print(isinstance(a, B))

# 检测一个对象是否有成员xxx
print(hasattr(a, "name"))

# 获取对象的所有方法属性和成员列表
print(dir(a))
