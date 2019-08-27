from urllib import request

if __name__ == '__main__':
    url = 'https://guangdiu.com/detail.php?id=6637916'
    # 打开一个URL然后返回页面的内容
    rsp = request.urlopen(url)
    # 把返回的结果读取出来，直接读取的是字节，默认是Unicode
    html = rsp.read()
    print(type(html))
    # 返回的字节，需要解码，解码以后是字符串,默认是UTF-8
    content = html.decode()
    # print(content)
    print(type(content))
