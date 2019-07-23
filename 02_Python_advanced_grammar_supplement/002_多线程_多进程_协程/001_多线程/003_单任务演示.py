# -*- coding:utf-8 -*-

from time import sleep

def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == '__main__':
    sing() #唱歌
    dance() #跳舞


# 运行代码，发现：
# 很显然刚刚的程序并没有完成唱歌和跳舞同时进行的要求
# 如果想要实现“唱歌跳舞”同时进行，那么就需要一个新的方法，叫做：多任务
