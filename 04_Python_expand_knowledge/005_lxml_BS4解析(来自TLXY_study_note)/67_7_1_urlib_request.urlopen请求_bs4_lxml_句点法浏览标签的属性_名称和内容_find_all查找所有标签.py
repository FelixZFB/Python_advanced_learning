# BeautifulSoup4的用法

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read() # <class 'bytes'>

# 创建一个bs的实例，bs4可以接收字符串也可以接收字节
# lxml是指使用的 lxml HTML 解析器
soup = BeautifulSoup(content, 'lxml')

# 调用prettify()方法。这个方法可以把要解析的字符串以标准的缩进格式输出。
# 这里需要注意的是，输出结果里面包含body和html节点，
# 也就是说对于不标准的HTML字符串BeautifulSoup，可以自动更正格式。
# 这一步不是由prettify()方法做的，而是在初始化BeautifulSoup时就完成了。
soup.prettify()


# 浏览属性
# 查看title标签所有内容
print(soup.title)
# 查看title标签的名称
print(soup.title.name)
# 查看标签内部的文字内容
print(soup.title.string)

# print(soup.find_all('a'))
# 从文档中找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))



