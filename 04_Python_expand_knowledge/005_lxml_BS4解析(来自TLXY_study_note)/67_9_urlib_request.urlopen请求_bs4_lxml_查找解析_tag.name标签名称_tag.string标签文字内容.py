# BeautifulSoup4的用法
# tag标签使用

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

# 创建一个bs的实例
# lxml是指使用的 lxml HTML 解析器
soup = BeautifulSoup(content, 'lxml')

# bs4可以自动转码
content = soup.prettify()


# tag标签浏览属性
print(soup.title)
print(soup.title.name)

# 标签对应的内容的值
print(soup.title.string)

#
print(soup.name)