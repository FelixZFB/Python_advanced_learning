# 遍历文档树

html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

# 上述文档中，缺少一些结束标签，BS会自动补全,补全后内容参考67_12.html文件
soup = BeautifulSoup(html_doc, 'lxml')
# print(soup)

# 查看子节点
print(soup.head)
print(soup.title)

# 获取<body>标签中的第一个<b>标签,b为字体加粗标签
print(soup.body.b)

# 所有的<a>标签,或是通过名字得到比一个tag更多的内容的时候，用find_all
# find_all，返回的是一个列表
print(soup.find_all('a'))

# 第一个body标签中，a标签的所有属性，返回的是一个字典
print(soup.body.a.attrs)
