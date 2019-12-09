# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/9 12:33
Desc:
'''

'''
策略指的就是为了达到某一目的而采取的多种手段或者方法。

为了实现软件设计，对象可能会用到多种多样的算法(逻辑)。
这些算法甚至会经常改变。如果将这些算法都硬编码到对象中，将会使得对象本身变得臃肿不堪，

策略模式很好的实现了将算法与本身对象解耦，从而避免出现上述的问题。

因此策略模式可以定义为：　定义一系列算法(逻辑)，
将每一个算法封装起来(一个算法创建一个类)，并让它们可以相互替换。
此模式让算法的变化,不会影响到使用算法的客户.

策略模式的结构

策略模式包含以下3个角色：

Context（环境类）

Strategy（抽象策略类）

ConcreteStrategy（具体策略类）

练习1：假设某司维护着一些客户资料，需要在该司有新产品上市或者举行新活动时通知客户。
现通知客户的方式有两种：短信通知、邮件通知。
应如何设计该系统的客户通知部分？为解决该问题，
我们先构造客户类，包括客户常用的联系方式和基本信息，同时也包括要发送的内容。

'''

# 抽象策略类
class MsgSender(object):
    type = ''  # 通知方式,用来保存电话号码或者邮箱地址
    info = ''  # 保存通知的内容

    def send(self):
        pass

# 具体策略类
class PhoneSend(MsgSender):
    def send(self):
        print('给{}打电话说:{}'.format(self.type, self.info))

# 具体策略类
class EmailSend(MsgSender):
    def send(self):
        print('给{}发邮件内容:{}'.format(self.type, self.info))

# 环境类
class Customer(object):
    name = ''
    tel = ''
    email = ''
    send_way = None

    # 设置发送方式
    def set_send_way(self, send_way):
        self.send_way = send_way

    def send_msg(self):
        self.send_way.send()

if __name__ == '__main__':
    # 创建用户，添加信息
    customer = Customer()
    customer.name = '六六'
    customer.tel = '111'
    customer.email = '555@'
    # 打电话通知
    phone_send = PhoneSend()
    customer.set_send_way(phone_send)
    phone_send.type = customer.name
    phone_send.info = '你迟到了！罚款200元'
    customer.send_msg()  # 给六六打电话说:你迟到了！罚款200元

    # 发短信
    email_send = EmailSend()
    customer.set_send_way(email_send)
    email_send.type = customer.name
    email_send.info = '你迟到了！罚款200元'
    customer.send_msg()  # 给六六发邮件内容:你迟到了！罚款200元