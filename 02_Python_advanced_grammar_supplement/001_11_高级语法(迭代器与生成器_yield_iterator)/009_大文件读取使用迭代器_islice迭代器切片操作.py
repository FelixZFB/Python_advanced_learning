# -*- coding:utf-8 -*-

# 打开文件使用readlines读取，按行读取为一个列表
# 但是，readlines读取全部内容到内存中
# 文件小没问题，但是文件太大，比如几个G，直接读取就会内存不足
with open('009_filetest.txt', 'r') as f:
    lines = f.readlines()
    print(lines[103:105])
print("*" * 50)


# 可以使用for循环迭代协议，避免内存不足
# with打开文件后会自动关闭，需要再次打开
# with open('009_filetest.txt', 'r') as f:
    # for line in f:
        # print(line)

# 迭代器切片操作，使用islice
from itertools import islice

# islice返回一个生成器函数，进行切片操作
with open('009_filetest.txt', 'r') as f:
    for line in islice(f, 103, 105):
        print(line)
    print("*" * 50)
    for line in islice(f, 5): #只给一个参数，指定的是结束的位置
        print(line)
    print("*" * 50)