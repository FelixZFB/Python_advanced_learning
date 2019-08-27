# 访问一个网址
# 对自己的UserAgent进行伪装

from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:

        # 伪装的方法有两种
        # 方法1：字典添加UA值
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D)'
        # 创建请求实例
        req = request.Request(url, headers=headers)

        # 方法2：req.add_header添加UA值,两个参数
        # req = request.Request(url)
        # req.add_header('User-Agent', 'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D)')

        # 打开实例
        rsp = request.urlopen(req)
        # 读取解码得到网页内容,读取到的是字节，编码后才是字符串
        html = rsp.read().decode()
        print(html)
        print(type(html))

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

    print("Done>----------")



