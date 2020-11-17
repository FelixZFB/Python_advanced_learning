# 搜索文档树
# find_all参数的传入
# find_all( name , attrs , recursive , string , **kwargs )

from bs4 import BeautifulSoup
import re

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# name参数
print(soup.find_all("title"))

# keyword 参数
print(soup.find_all(id='link2'))
print(soup.find_all(href=re.compile(r"elsie")))

# 传入true,查找所有带id的属性，并且返回一个列表
print(soup.find_all(id=True))

# 字典参数来搜索包含特殊属性的tag

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'lxml')

print(data_soup.find_all(attrs={"data-foo": "value"}))

