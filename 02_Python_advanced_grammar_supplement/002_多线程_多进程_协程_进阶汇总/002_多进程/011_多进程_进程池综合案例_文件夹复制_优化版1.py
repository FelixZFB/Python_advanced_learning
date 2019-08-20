# -*- coding:utf-8 -*-
# 复制一个文件夹，文件夹中有大量文件（成千上万的文件）

import os, time
import multiprocessing
from multiprocessing import Manager


def copy_file(q, file_name, old_folder_name, new_folder_name):

    old_file = open(old_folder_name + '/' + file_name, 'rb')
    content  = old_file.read()
    old_file.close()

    new_file = open(new_folder_name + '/' + file_name, 'wb')
    new_file.write(content)
    new_file.close()

    # 如果复制完了文件，就向队列中写入一个消息，表示该文件已经复制完成
    q.put(file_name)

    # 加入等待时间，便于观察，发现每次同时进行了三个任务
    time.sleep(1)


def main():
    # 1. 获取用户要copy的文件夹的名字
    old_folder_name = input('请输入要要copy的文件夹的名字: ')

    # 2. 创建一个新的文件夹，以旧文件夹名称为基准重命名后创建，如果存在就跳过
    try:
        new_folder_name = old_folder_name + '[复件]'
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹中所有待copy的文件名字,listdir返回文件夹中所有文件名称的列表
    file_names = os.listdir(old_folder_name)

    # 4. 创建进程池
    po = multiprocessing.Pool(3)

    # 5. 创建消息队列
    q = Manager().Queue()

    # 6. 向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name, ))
    # 关闭进程池
    po.close()

    # 7. 显示出复制进度条
    # 加入循环一直取出数据,并显示进度条
    all_file_num = len(file_names)
    copy_file_num = 0

    while True:
        file_name_done = q.get()
        copy_file_num += 1
        copy_rate = copy_file_num / all_file_num * 100
        print('\r%scopy进度为：%.2f%% (%s)' % (old_folder_name, copy_rate, file_name_done), end='')
        if copy_file_num >= all_file_num:
            break


if __name__ == '__main__':
    main()