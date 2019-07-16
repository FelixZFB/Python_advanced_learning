# 基本队列，先进先出

import queue
import time

q = queue.Queue()

for i in range(5):
    q.put(i)
    print(i)

while not q.empty():
    print(q.get())
    time.sleep(3)