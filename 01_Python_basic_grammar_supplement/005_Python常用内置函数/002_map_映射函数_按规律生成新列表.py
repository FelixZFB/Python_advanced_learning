# map: 映射
# 即把集合或者列表中的元素，每一个元素都按照一定的规则进行操作，生成一个新的列表或者集合
# map函数是系统提供的具有映射功能的高阶函数，返回值是一个迭代对象

# 先看一个列表[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，以该列表为基础每个数字乘以10
# 生成一个新的列表[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# 代码如下：
l1 = [i for i in range(10)]
l2 = []
for i in l1:
    l2.append(i * 10)

print(l1)
print(l2)


# map函数实现上面的功能，代码变的更简单
l3 = [i for i in range(10)]
def mulTen(n):
    return n * 10
l4 = map(mulTen, l3)


print(type(l4))
print(l4)

# map类型是可迭代的，使用for循环取出每个元素
for i in l4:
    print(i)
