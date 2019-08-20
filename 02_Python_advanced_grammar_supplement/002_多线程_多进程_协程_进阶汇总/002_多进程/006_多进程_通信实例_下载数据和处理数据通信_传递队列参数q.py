# -*- coding:utf-8 -*-

import multiprocessing


def download_data_from_web(q):
    '''下载得的的数据'''
    # 模拟从网上下载得到的数据
    data = [11, 22, 33, 44, 55]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)
    print('下载器已经下载完数据，并且将以下数据已经存入到队列中......')
    print(data)


def analysis_data(q):
    '''数据处理'''
    # 创建一个空列表，使用list()比[]更好，可读性更强
    new_data = list()

    # 从队列中取出数据,加入到待处理数据列表中
    while True:
        data = q.get()
        data += 11
        new_data.append(data)
        # 如果数据为空，结束
        if q.empty():
            break
    # 处理以后的数据
    print('处理之后的数据')
    print(new_data)


def main():
    # 1. 创建一个空队列
    q = multiprocessing.Queue()

    # 2. 创建多个进程，将队列作为实参传递到进程函数里去,传入参数是元组，逗号不能丢
    p1 = multiprocessing.Process(target=download_data_from_web, args=(q, ))
    p2 = multiprocessing.Process(target=analysis_data, args=(q, ))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()

# redis消息队列就是底层就是利用的q队列
