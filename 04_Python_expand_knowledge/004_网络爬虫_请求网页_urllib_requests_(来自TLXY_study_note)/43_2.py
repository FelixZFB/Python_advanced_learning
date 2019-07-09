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
    html = rsp.read()
    print(type(html))
    # 利用chardet检测编码
    # 类型是一个字典，字典中有采用的编码
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 返回的字节，需要解码
    # 使用get函数获得不会出错，有自己的编码就用检测到的编码解码
    # 如果没有检测到，就采用utf-8解码
    html = html.decode(cs.get('encoding', 'utf-8'))
    print(html)