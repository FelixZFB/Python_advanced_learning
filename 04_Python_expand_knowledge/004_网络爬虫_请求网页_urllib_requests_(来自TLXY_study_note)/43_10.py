# 使用代理IP访问一个网站
# 选取一个不上的网站，防止IP被封，以后访问不了
# 网址：http://www.cnqiang.com/
# 免费代理IP网站：http://www.goubanjia.com/


from urllib import request, error

if __name__ == '__main__':

    url = 'http://www.cnqiang.com/'

    # 使用代理的步骤
    # 1.设置代理IP,进入代理网站选择一个IP:PORT
    proxy = {'http': '47.97.190.145:9999'}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)

    # 现在如果访问url,就会使用代理服务器
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

