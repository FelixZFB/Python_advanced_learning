# js加密案例
# 破解有道在线翻译http://fanyi.youdao.com/的加密过程

from urllib import request, parse
import urllib
import json

if __name__ == '__main__':

    key = input("请输入需要翻译的文字: ")

    # 打开有道在线翻译，输入girl，检查，找到headers,复制里面的网址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    # 将网页中的Form Data中的所有数据复制出来
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15477305260619',
        'sign': 'c009854ee2557381432d80de4b37124b',
        'ts': '1547730526061',
        'bv': '9496786132714646371d4ce055f343c3',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }

    # 对data中的数据需要转换为bytes格式
    data = parse.urlencode(data).encode()

    # 将网页中的请求头Request Headers中的数据复制出来
    headers = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        # 'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '254',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1708526553 @ 10.168.8.61;JSESSIONID=aaaokcSwoACgIcdia7BHw;OUTFOX_SEARCH_USER_ID_NCOO=1780986461.6720798;___rl__test__cookies=1547730526054',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.26Safari/537.36Core/1.63.6788.400QQBrowser/10.3.2854.400',
        'X-Requested-With': 'XMLHttpRequest',
    }

    req = request.Request(url=url, data=data, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    print(type(html))
    print(html)





