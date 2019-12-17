# BeautifulSoup4的用法
# tag标签使用

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read() # 直接读取结果是字节
print(type(content))

# 创建一个bs的实例
# lxml是指使用的 lxml HTML 解析器
soup = BeautifulSoup(content, 'lxml')

# 调用prettify()方法。这个方法可以把要解析的字符串以标准的缩进格式输出。这里需要注意的是，输出结果里面包含body和html节点，也就是说对于不标准的HTML字符串BeautifulSoup，可以自动更正格式。这一步不是由prettify()方法做的，而是在初始化BeautifulSoup时就完成了。
soup.prettify()

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





