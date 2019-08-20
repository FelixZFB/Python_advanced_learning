# 多线程实例
# 多线程传递参数

import time
import _thread as thread

# 单线程实例

def loop1(in1):
    # ctime得到当前的时间
    print("Start loop 1 at: ", time.ctime())
    print("我是参数", in1)
    # 睡眠一定时间，单位是秒
    time.sleep(2)
    print("End loop 1 at: ", time.ctime())

def loop2(in1, in2):
    # ctime得到当前的时间
    print("Start loop 2 at: ", time.ctime())
    print("我是参数", in1, "和参数", in2)
    # 睡眠一定时间，单位是秒
    time.sleep(3)
    print("End loop 2 at: ", time.ctime())

def main():
    print("Starting at: ", time.ctime())
    # 启动一个多线程，()中是放前面函数的参数的
    # 只有一个参数，后面的逗号要写上，才代表一个元组touple
    thread.start_new_thread(loop1, ("Felix", ))
    # 再启动一个多线程
    thread.start_new_thread(loop2, ("Fang", "Bai"))
    time.sleep(6)
    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()


