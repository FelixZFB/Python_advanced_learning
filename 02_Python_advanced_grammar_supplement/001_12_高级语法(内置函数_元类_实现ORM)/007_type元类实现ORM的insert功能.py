# -*- coding:utf-8 -*-

# 创建一个自定义的元类，继承type类就是元类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是指定的StringField或者IntegerField的实例对象
            # k ---> uid
            # v ---> ('uid', "int unsigned")
            if isinstance(v, tuple):
                # print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 删除这些已经在字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将之前的uid/name/email/password以及对应的对象引用、类名字
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# __new__函数的作用就是创建一个实例对象，给它分配一个内存空间
# 创建普通类时，一般不写，先调用__new__函数，然后调用__init__函数
# 指定metaclass=ModelMetaclass，使用上面的ModelMetaclass元类来创建这个User类
# 创建User类时，调用元类的__new__函数，attrs就是下面User的类属性（是一个字典）,等号左边键，右边是值
# 元类，先创建一个空字典，然后遍历User类属性，添加到mappings字典中，接着再次循环，删除掉attrs中本来的类属性
# 最后attrs字典中添加两个键值，__mappings__键对应的值就是一个字典mappings，里面存储着所有的类属性
# __table__对应的类的名字User
# 使用元类完成了一件事，删除了attrs原有的类属性，将类属性就自动转变成了__mappings__和__table__两个键值属性了

# User类中的类属性才是开发常规写法，经过元类的转换，类属性就删除了，自动进行了转变
# 我们给User实例传递参数时候，还是按照类属性的格式书写

class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")
    # 当指定元类之后，以上的类属性将不在类中，而是在__mappings__属性指定的字典中存储
    # 以上User类中有
    # __mappings__ = {
    #     "uid": ('uid', "int unsigned")
    #     "name": ('username', "varchar(30)")
    #     "email": ('email', "varchar(30)")
    #     "password": ('password', "varchar(30)")
    # }
    # __table__ = "User"
    # 使用元类以后，类属性就自动转变成了__mappings__和__table__两个键值属性了
    # 上面等号左边是键，右边是值

    # 以字典的方式接受所有的不定关键字参数
    def __init__(self, **kwargs):
        # 传进来的参数作为字典存储在kwargs, uid=12345.....
        for name, value in kwargs.items():
            # 设置attrs属性，name=value，即：uid=12345， name='Michael'......
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        # 现在实例中找，没有，就到类中去找，找到了上面的__mappings__
        # k='uid' v=('uid', "int unsigned")
        for k, v in self.__mappings__.items():
            fields.append(v[0])  # 元组第一个元素v[0]='uid'
            args.append(getattr(self, k, None)) # 获取self实例对象k=uid对应的属性值，即12345
        # 经过循环，fields=['uid', 'name',...]，args=[12345, 'Michael',...]

        # 使用join函数将列表中每个元素连接在一起，使用逗号连接，变成SQL格式的语句
        # 但是
        # self.__table__现在实例属性中找没有，就去类属性中去找
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)
        # SQL: insert into User (uid,username,email,password) values (12345,Michael,test@orm.org,my-pwd)

# 上面通过元类，实现了类属性的映射


# 实例化对象，__new__方法创建对象，__init__方法对象创建是自动执行，self指向的就是该实例对象
u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(u.__class__) # 查看u属于哪个类
print(u.__dict__) # 查看u的属性
u.save()


# 上面过程就实现了ORM功能，直接使用属性，最后就得到了映射的SQL语句
# 但是上面User中实现映射的功能可以单独变成一个基类中，最后用户的类只留下要输入的属性即可
# 参考案例008
