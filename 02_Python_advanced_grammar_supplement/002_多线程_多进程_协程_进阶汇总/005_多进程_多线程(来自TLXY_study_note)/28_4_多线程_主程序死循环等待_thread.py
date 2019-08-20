# 多线程实例
# 28_1.py单线程改写为多线程
# 多线程2，查看结果
# 主程序执行完毕添加一个睡眠时间，等待loop1和loop2执行完

import time
import _thread as thread

# 单线程实例

def loop1():
    # ctime得到当前的时间
    print("Start loop 1 at: ", time.ctime())
    # 睡眠一定时间，单位是秒
    time.sleep(2)
    print("End loop 1 at: ", time.ctime())

def loop2():
    # ctime得到当前的时间
    print("Start loop 2 at: ", time.ctime())
    # 睡眠一定时间，单位是秒
    time.sleep(3)
    print("End loop 2 at: ", time.ctime())

def main():
    print("Starting at: ", time.ctime())
    # 启动一个多线程，()中是放前面函数的参数的
    thread.start_new_thread(loop1, ())
    # 再启动一个多线程
    thread.start_new_thread(loop2, ())
    print("All done at: ", time.ctime())



if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)



