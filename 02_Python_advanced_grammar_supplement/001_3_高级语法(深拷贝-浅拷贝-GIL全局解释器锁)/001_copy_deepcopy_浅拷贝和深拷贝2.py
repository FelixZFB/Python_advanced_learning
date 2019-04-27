# 3. copy.copy:浅拷贝，只拷贝引用，
# 列表中的每个元组，只拷贝每个元素的指向内存地址的引用
# copy与赋值不同，赋值是变量当做一个整体拷贝了引用
import copy
a = [11, 22]
d = copy.copy(a)
print()
print(id(a))
print(id(d))
print(id(a[1]))
print(id(d[1]))
# 输出结果显示，a和d的地址并不同，因为d并不是浅拷贝的a这个整体
# 拷贝的是里面每个元素地址的引用

# 4. 浅拷贝补充

a = [11, 22]
b = [33, 44]
c = [a, b]
d = c #d指向c，浅拷贝
e = copy.copy(c) # e拷贝的是c里面a和b地址的引用
print()
print(e)
print(id(c))
print(id(d))
print(id(e))
# 输出结果显示，e并不是指向c的地址

print()
print(id(a))
print(id(e[0]))
print(id(b))
print(id(e[1]))
# 输出结果显示，e指向的是a和b的地址
