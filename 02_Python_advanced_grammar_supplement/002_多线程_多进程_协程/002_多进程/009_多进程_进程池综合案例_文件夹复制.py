# -*- coding:utf-8 -*-

# 复制一个文件夹，文件夹中有大量文件（成千上万的文件）
# 进程池实现多任务

import os
import multiprocessing


def main():
    # 1. 获取用户要copy的文件夹的名字
    # （当前目录下，直接输入文件夹名称，
    # 不在当前路径下，将文件夹路径复制后输入
    # 会自动打开路径下的文件夹）
    # 以当前目录下：009案例测试文件夹作为测试文件夹
    old_folder_name = input('请输入要要copy的文件夹的名字: ')
    print(old_folder_name)

    # 2. 创建一个新的文件夹
    os.mkdir(old_folder_name + '[复件]')

    # 3. 获取文件夹中所有待copy的文件名字,listdir返回文件夹中所有文件名称的列表
    file_names = os.listdir(old_folder_name)
    print(file_names)


if __name__ == '__main__':
    main()