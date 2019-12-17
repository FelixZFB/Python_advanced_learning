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
print(type(soup))

# 格式化soup，每个标签独占一行
soup.prettify()
# print(soup)

# tag标签浏览属性
print(soup.title) # 获取整个标签内容
print(soup.title.name)  # 获取标签的名称

# 获取tag标签的所有属性
print(soup.title.attrs) # 属性为空

# 标签对应的内容的值
print(soup.title.string) # 获取标签中的内容

# 整个soup的name即[document]
print(soup.name)