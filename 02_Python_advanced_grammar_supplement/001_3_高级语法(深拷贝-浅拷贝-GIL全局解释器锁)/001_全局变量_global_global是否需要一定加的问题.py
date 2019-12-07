# 在一个函数中对全局变量进行修改的时候，是否需要使用global进行说明：
# 要看是否对全局变量的执行: 指向内存地址进行了修改
# 如果修改了指向地址，即让全局变量指向了一个新的地方(内存地址),那么必须使用global，类似于深拷贝
# 如果仅仅修改了指向空间中的数据，指向的内存地址不变，此时不用必须使用global，类似于浅拷贝

# 看下面代码，+=修改了指向地址
# 列表内置函数只修改数据，指向地址不变

num = 100
nums = [100, 200]

# 修改了指向地址
def test1():
    global num
    num += 100

# append.insert.等内置函数，指向地址不变
def test2():
    nums.append(300)

# 修改了指向地址
def test3():
    global nums
    nums += [100, 200]

# 先打印数据
print(num)
print(nums)

# 执行函数后再次打印数据对比
print('*************')
test1()
test2()
print(num)
print(nums)


print('*************')
test3()
print(nums)


