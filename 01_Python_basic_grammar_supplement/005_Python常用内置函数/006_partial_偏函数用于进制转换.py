# 偏函数最常用地方：进制转换
# 进制转换int函数，包含关键字参数base

from functools import partial

# 把字符串转化为十进制数字,base默认转换为十进制
print(int("123"))
print(int("123", base=10))
print(int("123", base=8))


print("------------")
# 使用偏函数生成一个新函数，第一个参数为原函数名int，第二个参数为关键字参数base
# 实现上面字符串转换为各种进制的功能
int2 = partial(int, base=2)
print(int2("1010"))

int8 = partial(int, base=8)
print(int8("123"))

int16 = partial(int, base=16)
print(int16("123"))