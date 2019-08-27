# URLError的使用

from urllib import request, error

if __name__ == '__main__':

    # 输入一个错误网址
    url = 'http://www.sipo.gov.cn/www'
    # 下面网址会自动跳转
    # url = 'http://www.22222fdadfafddddddu.com'

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)

    # 错误并没有执行，执try时候网页自动跳转了，跳转到了一个新网页
    # 为了显示错误的结果：
    # 方法1：可以把网断掉，然后再次执行，结果如下
    # URLError: [Errno 11001] getaddrinfo failed
    # URLError: <urlopen error [Errno 11001] getaddrinfo failed>
    # 方法2：将url替换为一个政府的错误网址，结果如下
    # HTTPError: Not Found
    # HTTPError: HTTP Error 404: Not Found
