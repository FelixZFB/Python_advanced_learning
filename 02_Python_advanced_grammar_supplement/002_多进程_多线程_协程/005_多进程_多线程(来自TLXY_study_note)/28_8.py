# 守护线程实例

import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

# 设置一个多线程
t1 = threading.Thread(target=fun, args=())
# 设置守护线程，必须在start之前，否则无效
# 主线程睡1秒，子线程睡2秒，睡眠中就结束了
# 子线程只开始了，但是主线程已经结束了，子线程没有结束就被干掉了
# 子线程没有end fun
# 设置了守护线程，主线程结束，子线程没有执行完毕也直接结束
t1.setDaemon(True)
t1.start()

time.sleep(1)
print("Main thread end")


