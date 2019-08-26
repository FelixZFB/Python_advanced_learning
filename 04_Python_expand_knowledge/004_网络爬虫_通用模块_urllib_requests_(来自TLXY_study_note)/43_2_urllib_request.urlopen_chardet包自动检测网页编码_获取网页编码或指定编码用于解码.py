# chardet
# 自动检测URL编码

# 手动进入网页源码，meta标签的charset属性指定的有编码格式

import chardet
from urllib import request

if __name__ == '__main__':
    url = 'http://china.chinadaily.com.cn/a/201901/15/WS5c3d510fa31010568bdc3902.html'
    # 打开一个URL然后返回页面的内容
    rsp = request.urlopen(url)
    # 把返回的结果读取出来
    # <class 'http.client.HTTPResponse'>
    print(type(rsp))
    html = rsp.read()
    # 直接读取的html是字节格式 <class 'bytes'>
    print(type(html))
    # 利用chardet检测编码
    # 类型是一个字典，字典中有采用的编码
    cs = chardet.detect(html)
    print(type(cs)) # <class 'dict'>
    print(cs) # {'encoding': 'utf-8',....}

    # 获取网页编码用于解码
    # 返回的字节，需要解码
    # 使用get函数获得不会出错，get函数获取到的编码，就用检测到的编码解码
    # 如果没有检测到，就采用utf-8解码
    html = html.decode(cs.get('encoding', 'utf-8'))
    print(html)