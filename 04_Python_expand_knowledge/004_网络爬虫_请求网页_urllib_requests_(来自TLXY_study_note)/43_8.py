# HTTPError的使用

from urllib import request, error

if __name__ == '__main__':

    # 输入一个错误网址
    url = 'http://www.sipo.gov.cn/www'

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
        print("HTTPError: {0}".format(e))


    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)