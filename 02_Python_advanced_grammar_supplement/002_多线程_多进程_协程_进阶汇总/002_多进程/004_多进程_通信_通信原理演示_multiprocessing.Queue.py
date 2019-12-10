# -*- coding:utf-8 -*-

from multiprocessing import Queue

#初始化一个Queue对象，最多可接收三条put消息
q=Queue(3) # 消息容量3
q.put("消息1")
q.put("消息2")

print(q.full())  # 还只放2条消息，没有满False

q.put("消息3")

print(q.full()) #True

# 因为消息列队已满下面的try都会抛出异常，
# 第一个try会等待2秒后再抛出异常，第二个Try会立刻抛出异常
# put函数有一个参数block默认为True，如果已经没有空间可写入，
# 此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间为止，
# 如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；
# 因此使用try函数，消息满了，超时2秒，然后执行下面的except语句
try:
    q.put("消息4",True,2)
except:
    print("消息列队已满，现有消息数量:%s" % q.qsize())

try:
# 如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常
# Queue.put_nowait(item)：相当Queue.put(item, False)
# 立即抛出异常
    q.put_nowait("消息4")
except:
    print("消息列队已满，现有消息数量:%s" % q.qsize())



#推荐的方式，先判断消息列队是否已满，再写入
if not q.full():
    q.put_nowait("消息4")

#读取消息时，先判断消息列队是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        # 如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；
        # Queue.get_nowait()：相当Queue.get(False)
        print(q.get_nowait())