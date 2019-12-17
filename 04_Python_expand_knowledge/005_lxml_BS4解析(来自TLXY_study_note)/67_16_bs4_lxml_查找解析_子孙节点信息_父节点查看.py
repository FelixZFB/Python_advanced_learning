# 遍历文档树
# 父节点

from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

head_tag = soup.head
title_tag = soup.head.title
print(head_tag)
print(title_tag)
print(title_tag.string)
print("*" * 50)


# 查看title的父节点,输出的是父节点的所有内容
print(title_tag.parent)
print(title_tag.parent.name)
print("*" * 50)


# 查看字符串的父节点
print(title_tag.string.parent)
print(title_tag.string.parent.name)
print("*" * 50)

# 顶端标签html也有父节点,就是整个bs4文档对象
print(type(soup.html.parent))
print(soup.html.parent.name)
print("*" * 50)

# bs4对象没有父节点了
print(soup.parent)
print("*" * 50)


