# -*- coding:utf-8 -*-

# 专门用于逻辑处理，与Web服务器进行分开

import time

def login():
    return '-----login-----welcome to our website-----time: %s' % time.ctime()

def register():
    return '-----register-----welcome to our website-----time: %s' % time.ctime()

def profile():
    return '-----profile-----welcome to our website-----time: %s' % time.ctime()

def application(file_name):
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    else:
        return 'not found this page...'
