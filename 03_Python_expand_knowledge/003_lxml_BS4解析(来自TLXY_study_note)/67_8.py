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


# 实际meta,link标签有很多，但是只会打印第一个
print(soup.meta)
print(soup.link)

# 直接获取某个标签中属性的值
print(soup.link['type'])
# 如果属性里面有多个值，返回的就是一个列表
print(soup.link['rel'])

# 查看link的名称
print(soup.link.name)

# attrs就是link的所有属性，会做成一个字典，没有顺序
print(soup.link.attrs)

# 修改type属性的值
soup.link.attrs['type'] = 'image'
print(soup.link)





