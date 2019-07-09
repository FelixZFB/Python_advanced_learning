# 多线程实例
# 先写一个单线程

import time

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
    loop1()
    loop2()
    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()


