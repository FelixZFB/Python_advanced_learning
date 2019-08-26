
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


# 访问私有变量的方法
# 采用字典查看age对应的变量名称为：_Person__age
print(Person.__dict__)

# 访问私有变量
print(p._Person__age)



