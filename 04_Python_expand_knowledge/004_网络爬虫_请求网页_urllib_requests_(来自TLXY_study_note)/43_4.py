from urllib import request, parse

if __name__ == '__main__':

    # 百度搜索请求头信息
    url = 'http://www.baidu.com/s?'
    wd = input('Input your keyword: ')

    # 要想使用data,需使用字典结构
    qs = {'wd': wd}

    # 将输入的字典qs转换为url编码
    # 可以将打印出来的和百度搜索访问结果图片43_4中进行对比，发现url编码是一样的
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # 访问的网址必须转换为url编码，直接访问会报错
    # fullurl = 'http://www.baidu.com/s?wd=大熊猫'
    rsp = request.urlopen(fullurl)

    html = rsp.read()
    html= html.decode()
    print(html)



