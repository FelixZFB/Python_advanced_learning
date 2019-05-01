# 类中创建property对象，可以传入四个参数：
# 第一个参数是方法名，调用 实例对象.property对象 时自动触发执行方法
# 第二个参数是方法名，调用 实例对象.property对象 ＝ XXX 时自动触发执行方法
# 第三个参数是方法名，调用 del 实例对象.property对象 时自动触发执行方法
# 第四个参数是字符串，调用 类名.property对象.__doc__ ，此参数是该属性的描述信息
# 一般都只使用前面两个参数，参考下面案例中调用时候的写法

#coding=utf-8
class Foo():

    def __init__(self):
        pass

    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数,self和属性的值"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    # 创建一个property对象吗，传入四个参数
    BAR = property(get_bar, set_bar, del_bar, "我是说明文档description...")

# 创建一个实例对象
obj = Foo()

res = obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
print(res)

obj.BAR = "alex"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入

desc = Foo.BAR.__doc__  # 自动获取第四个参数中设置的值：description...
print(desc)

del obj.BAR  # 自动调用第三个参数中定义的方法：del_bar方法
