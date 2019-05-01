# class A(object)经典类中的属性只有一种访问方式，其对应被 @property修饰的方法
# class A()新式类中的属性有三种访问方式，并分别对应了
# 三个被 @ property、@方法名.setter、@方法名.deleter修饰的方法

# 由于新式类中具有三种访问方式，我们可以根据它们几个属性的访问特点，
# 分别将三个方法定义为对同一个属性：获取、修改、删除

class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    # 获取价格
    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    # 修改价格，必须两个参数,self和属性的值
    @price.setter
    def price(self, value):
        self.original_price = value

    # 删除原价格
    @price.deleter
    def price(self):
        del self.original_price

obj = Goods()
print(obj.original_price)
# 以下代码自动执行@property修饰的price方法，并获取方法的返回值
obj.price     # 获取商品价格
# 以下代码自动执行@price.setter修饰的price方法，并将200赋值给方法的参数value
obj.price = 200   # 修改商品原价
print(obj.original_price)
# 以下代码自动执行@price.deleter修饰的price方法，删除商品的原价
del obj.price     # 删除商品原价属性，属性就没有了

# 一般只使用获取价格和修改价格两种property属性，删除原价属性一般不用

