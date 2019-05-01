# python2中分经典类和新式类写法不一样：经典类里面要写object,新式类不用写,
# python3未区分，直接不写，因为python3中默认继承object类，都是新式类

# 类对象:就是一个类，只有一个
# 实例对象：类对象的实例化，可以有多个
# 类属性：属于类，实例对象共有的属性可以放在类属性中,可以直接通过类访问或者实例访问，比如country属性
# 实例属性：属于实例特有，每个实例的属性都不相同，比如name属性


# 类属性在内存中只保存一份
# 实例属性在每个对象中都要保存一份

# 应用场景：
# 通过类创建实例对象时，如果每个对象需要具有相同名字的属性，那么就使用类属性，用一份既可


# object可以写也可以不写
# 在python2中写object就是经典类，不写就是新式类

# 创建一个类对象
class Province(object):
    # 类属性，所有实例省份都属于中国，共有的属性
    country = '中国'
    # 初始化属性，用来接收实例中的参数
    def __init__(self, name):
        # 实例属性，实例特有，每个实例的name不相同
        self.name = name

# 创建第一个实例对象
obj1 = Province('山东省')
# 直接访问实例属性
print(obj1.name)

# 创建第二个实例对象
obj2 = Province('湖北省')
# 直接访问实例属性
print(obj2.name)


# 通过类直接访问类属性
print(Province.country)
# 通过实例对象访问类属性，两种访问方式
print(obj1.country)
print(obj1.__class__.country)




