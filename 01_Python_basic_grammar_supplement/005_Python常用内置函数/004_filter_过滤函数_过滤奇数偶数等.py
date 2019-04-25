# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

# 接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

# 实例1：过滤出列表中的所有奇数
# 定义得到奇数的方法，满足条件的就返回会布尔值True
# filter中满足判断条件为True的就加入到新列表中
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)
odd = []
for i in newlist:
    odd.append(i)
print(odd)

# 实例2：过滤出列表中的所有偶数
def is_even(n):
    return n % 2 == 0
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even = []
for i in newlist:
    even.append(i)
print(even)

# 实例3：过滤出1~100中平方根是整数的数:1,4,9......81,100
import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0
newlist = filter(is_sqr, range(1, 101))
l = []
for i in newlist:
    l.append(i)
print(l)