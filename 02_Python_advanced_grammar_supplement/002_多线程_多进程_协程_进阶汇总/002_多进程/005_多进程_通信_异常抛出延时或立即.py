# -*- coding:utf-8 -*-

from multiprocessing import Queue

#初始化一个Queue对象，最多可接收三条put消息
q=Queue(3)
q.put("消息1")

# 先取出第一条消息
print(q.get(True, 5))
# 延时5秒后抛出异常
# print(q.get(True, 5))

# 立即抛出异常的两种方式
# print(q.get(False))
print(q.get_nowait())