# -*- coding:utf-8 -*-

# 专门用于逻辑处理，与Web服务器进行分开
# application()函数就是符合WSGI标准的一个HTTP处理函数
# 加入charset=utf-8就可以支持中文了

# 002升级版，相当于加入dict传递参数，合并加入001中的mini_frame的功能

import time

def login():
    return '-----login-----welcome to our website-----当前时间: %s' % time.ctime()

def register():
    return '-----register-----welcome to our website-----当前时间: %s' % time.ctime()

def profile():
    return '-----profile-----welcome to our website-----当前时间: %s' % time.ctime()


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8'), ('Connection', 'keep-alive')])

    file_name = environ['PATH_INFO']

    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    elif file_name == '/profile.py':
        return profile()
    else:
        return 'not found this page...请重试'


# Web服务器支持MSGI协议，整个代码动态请求的执行流程

# 1. 支持MSGI的Web框架里面必须有一个application函数，传入两个参数，
# environ：一个包含所有HTTP请求信息的dict对象，用于参数的传递，此处是传递的file_name
# start_response：一个发送HTTP响应的函数

# 2. Web服务器代码，获取到动态请求，即从else开始执行，先定义了一个空字典env
# 将动态请求的网页名file_name加入到字典中
# response_body调用了mini_frame.application方法，env作为第一个参数传入
# self.set_response_header是一个函数，作为第二个参数传入

# 3. 然后，application函数开始执行start_response('200 OK', [('Content-Type', 'text/html')])
# 此时的start_response就是执行服务器中的set_response_header函数
# '200 OK'作为第一个参数status
# [('Content-Type', 'text/html')]作为第二个参数headers
# 这两个参数设置为类属性，用于之后的调用

# application函数然后根据file_name的值调用相应的函数执行，
# 相应函数的返回值，赋值给response_body

# 4. 3执行完毕后，response_body已经有值了，接下来的代码是完成response_header
# response_header先得到第一行状态信息，然后再加一行Content-Type信息
# 然后空一行，之后拼接上body的信息

# 5. 发送响应报文

# 运行结果请查看图片：WSGI字典传递参数的运行结果

# 总结：
# MSGI的application函数，函数本身返回值完成了body信息
# 里面的一个函数完成了header信息，最终实现了响应报文
# 函数名和返回的信息都是自定义的，可以自己修改
# 这样就实现了服务器和框架的分离
# mini_frame里面写什么代码，最终响应报文就是什么




