# -*- coding:utf-8 -*-


from greenlet import greenlet
import time

def test1():
    while True:
        print("---A--")
        gr2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print("---B--")
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(test1)
gr2 = greenlet(test2)


# greenlet里面已经封装了yield方法
# 将创建的gr1交叉插入到函数里面，用于切换运行多任务
# 切换到gr1中运行
gr2.switch()

# greenlet已经实现了协程，但是这个还的人工切换
# 不推荐使用,推荐使用gevent，看案例014