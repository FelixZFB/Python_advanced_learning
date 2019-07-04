# -*- coding:utf-8 -*-

import re

def check_email_address():

    email = input('请输入邮箱地址:')
    # 如果正则表达式需要使用特殊字符：.?+等需要前面添加\反斜杠进行转义
    # 代表一个普通字符
    ret = re.match(r'[a-zA-Z0-9]{6,12}@163\.com$', email)

    if ret:
        print("%s 符合要求" % email)
    else:
        print("%s 不符合要求" % email)

if __name__ == '__main__':
    check_email_address()