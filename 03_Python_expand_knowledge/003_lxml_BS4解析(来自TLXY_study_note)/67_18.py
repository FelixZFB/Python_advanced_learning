# 搜索文档树


from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# 找出所有的b标签
print(soup.find_all('b'))

# 正则表达式,re.compile(r'^b')为一个正则对象
# 找出所有以b开头的标签
import re
for tag in soup.find_all(re.compile(r'^b')):
    print(tag.name)

# 下面代码找出所有名字中包含”t”的标签
for tag in soup.find_all(re.compile(r't')):
    print(tag.name)

