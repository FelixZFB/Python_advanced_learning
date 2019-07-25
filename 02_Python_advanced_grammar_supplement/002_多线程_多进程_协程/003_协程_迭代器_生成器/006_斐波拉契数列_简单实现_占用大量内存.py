# -*- coding:utf-8 -*-


# 数学中有个著名的斐波拉契数列（Fibonacci），
# 数列中第一个数为0，第二个数为1，
# 其后的每一个数都可由前两个数相加得到：
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# 初始数据
a = 0
b = 1

# 生成
nums = list()
nums.append(a)

# a是前一个数，b是后一个数
a, b = b, a+b
# a=1 b=0+1
nums.append(a)

a, b = b, a+b
# a=1 b=1+1
nums.append(a)

a, b = b, a+b
# a=2 b=1+2
nums.append(a)

a, b = b, a+b
# a=3 b=2+3
nums.append(a)

a, b = b, a+b
# a=5 b=2+5
nums.append(a)

print(nums)


# 上面代码简化，使用while循环生成
nums = list()
a = 0
b = 1
nums.append(a)
while True:
    a, b = b, a + b
    nums.append(a)
    if len(nums) >= 10000:
        break

# print(nums)

for num in nums:
    print(num)

# 运行结果显示，将数字改大后，需要较长时间才出来出来结果
# 并且结果又是存在一个列表里面，占用了大量内存
# 任务管理器查看：cpu和内存占用很大，并且风扇都启动了

# 该案例先生成了大量数据nums，放到缓存之中
# 然后通过for循环从缓存中取出

# 007并不会生成大量数据，保存的是生成数据的方法




