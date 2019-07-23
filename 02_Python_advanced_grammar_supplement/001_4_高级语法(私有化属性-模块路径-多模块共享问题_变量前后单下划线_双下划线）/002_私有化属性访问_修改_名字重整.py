# 私有化属性本质：
# 类创建的时候，私有属性创建后，类内部实际上对该属性进行了名字重整

class Test(object):

    def __init__(self, name, age):
        self.name = name # 实例属性，外界可以访问
        self.__age = age # 私有属性，外界不能直接访问，内部可以访问

a = Test('Felix', 18)

# 访问实例属性
print(a.name)
# 访问私有属性
# print(a.__age) # 会提示无该对象，因为属性名字已经修改了
# 查看a对象的所有属性,发现__age已经被修改为单下划线加类的名字，_Test__age
print(a.__dict__)
# 访问私有属性
print(a._Test__age)
#




