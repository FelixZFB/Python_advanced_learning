# BeautifulSoup4的用法

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

# 创建一个bs的实例
# lxml是指使用的 lxml HTML 解析器
soup = BeautifulSoup(content, 'lxml')

# bs4的prettify()可以自动格式化后以Unicode编码输出
content = soup.prettify()
print(type(content))

# 查找的两种方法
title_tag = soup.select('title')
print(title_tag)
title_tag = soup.find_all('title')
print(title_tag)

# 根据标签名称和标签中的内容查找音乐这个链接
aaa = soup.find_all('a', string='音乐')
print(aaa)






