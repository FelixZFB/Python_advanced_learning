# BeautifulSoup4的用法

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
print(type(content))
# print(content)

# 浏览属性
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup.find_all('a'))
# 从文档中找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))



