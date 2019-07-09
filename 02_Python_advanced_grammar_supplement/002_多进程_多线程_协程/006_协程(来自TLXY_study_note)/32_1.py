# 迭代器实例

# l是可迭代的，但不是迭代器
l = [i for i in range(10)]
for idx in l:
    print(idx)

# range是个迭代器
for i in range(5):
    print(i)

# isinstance判断是否可迭代或者迭代器
from collections import Iterable, Iterator
ll = [1, 2, 3, 4, 5]
print(isinstance(ll, Iterable))
print(isinstance(ll, Iterator))

# 字符串是否可迭代
s = "i love you, you love me"
print(isinstance(s, Iterable))
print(isinstance(s, Iterator))

# iter转换可迭代的为迭代器
ss = iter(s)
print(isinstance(ss, Iterable))
print(isinstance(ss, Iterator))


# 生成器
# 中括号就是列表生成器
# 小括号就是生成器
L= [x*x for x in range(5)]
g = (x*x for x in range(5))
print(L)
print(g)
print(type(L))
print(type(g))

# 函数案例
def odd():
    print("Step 1")
    print("Step 2")
    print("Step 3")
    return None

odd()
print(type(odd()))


