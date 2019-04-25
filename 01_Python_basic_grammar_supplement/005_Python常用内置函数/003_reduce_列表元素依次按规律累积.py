
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果

# reduce实例：0到100求和

from functools import reduce

# 定义一个方法
def myAdd(x, y):
    return x + y
# 对于列表[1, 2, 3, ....]执行,前一个加后一个，一直向后加，直到结束返回一个值
# 0到100的数字相加求和
print([i for i in range(101)])

rst = reduce(myAdd, [i for i in range(101)])

print(rst)


# 上面功能可以使用lambda和reduce快速实现
rst = reduce(lambda x, y: x+y, [i for i in range(101)]) # 使用 lambda 匿名函数
print(rst)

