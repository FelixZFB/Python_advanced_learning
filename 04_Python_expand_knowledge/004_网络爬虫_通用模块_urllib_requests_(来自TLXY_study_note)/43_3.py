# chardet
# 自动检测URL编码

import chardet
from urllib import request

if __name__ == '__main__':
    url = 'http://china.chinadaily.com.cn/a/201901/15/WS5c3d510fa31010568bdc3902.html'
    # 打开一个URL然后返回页面的内容
    rsp = request.urlopen(url)
    # 把返回的结果读取出来
    print(type(rsp))
    print("URL: {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))
