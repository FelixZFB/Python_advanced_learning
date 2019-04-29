# **kwarg还有一个很漂亮的用法，就是创建字典：

# 传入多个关键关键字，返回kwargs，返回值就是一个字典
def kw_dict(**kwargs):
    print(kwargs)
    return kwargs

kw_dict(a=1, b=2, c=3)

# python自带字典功能
dict_1 = dict(a=1,b=2,c=3)
print(dict_1)

