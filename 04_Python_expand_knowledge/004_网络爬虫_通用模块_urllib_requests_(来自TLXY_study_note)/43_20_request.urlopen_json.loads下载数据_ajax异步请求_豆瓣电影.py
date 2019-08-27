# 爬取豆瓣电影
# 了解ajax请求（向下滚动网页，网页自动不停的更新）

import json
from urllib import request

if __name__ == '__main__':

    url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20'

    rsp = request.urlopen(url)

    # 读取网页数据，一般为json格式, 直接读取到的是bytes格式，解码后是一个str字符串格式
    data = rsp.read().decode()
    print(type(data))

    # json格式进行解码为python格式，发现是一个list
    data = json.loads(data)
    print(type(data))

    print(data)



