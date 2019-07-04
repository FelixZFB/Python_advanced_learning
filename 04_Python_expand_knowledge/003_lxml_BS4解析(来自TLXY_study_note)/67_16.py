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

print("\n")
# 查看title的父节点
print(title_tag.parent)
# 查看字符串的父节点
print(title_tag.string.parent)
# 顶端标签html也有父节点,就是整个bs4文档对象
print(type(soup.html.parent))
# bs4对象没有父节点了
print(soup.parent)


