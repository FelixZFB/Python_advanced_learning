# JS加密破解案例
# 有道在线翻译JS加密案例
# salt对应的值为i
# i = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10)
# 可以进入到console中查看i各部分计算的值是什么，参考43_19_1图片
# sign: n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")


import time, random
import hashlib
from urllib import request, parse
import urllib
import json



# 计算盐的值
def getSalt():

    '''将上述salt值i的公式翻译成python代码'''
    # 查看43_19_1图片
    # (new Date).getTime()发现时间值有十二位，单位应是ms，同时是个整数
    # 我们python得到的时间值是秒，要乘以1000，然后取整
    # parseInt(10 * Math.random(), 10)得到的是0,10之间的一个随机整数
    salt = int(time.time()*1000) + random.randint(0, 10)
    return salt

# 计算MD5的值的公式
def getMD5(v):

    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()

    return sign

# 计算sign的值
def getSign(key, salt):

    sign = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    sign = getMD5(sign)
    return sign

# 模拟有道翻译
def youdao(key):

    # 打开有道在线翻译，输入girl，检查，找到headers,复制里面的网址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    salt = getSalt()

    # 将网页中的Form Data中的所有数据复制出来
    data = {
        'i': key,
        'salt': str(salt),
        'sign': getSign(key, salt),
        'doctype': 'json',
    }

    print(data)

    # 对data中的数据需要转换为bytes格式
    data = parse.urlencode(data).encode()

    print(data)

    # 将网页中的请求头Request Headers中的数据复制出来
    headers = {
        'Content-Length': len(data),
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71',
    }

    req = request.Request(url=url, data=data, headers=headers)
    res = request.urlopen(req)

    # 下载导出数据
    result = json.loads(res.read())

    # 打印出翻译后的结果
    print(result)

if __name__ == '__main__':
    # key = input("请输入需要翻译的文字: ")
    youdao('boy')








