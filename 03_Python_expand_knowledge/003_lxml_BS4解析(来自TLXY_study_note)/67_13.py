# 遍历文档树
# 子孙节点信息

from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# .contents 属性可以将tag的子节点以列表的方式输出
head_tag = soup.head
print(head_tag.contents)
print(head_tag.contents[0])

title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

# soup下面也有子节点HTML
print(len(soup.contents))
print(soup.contents[0].name)

#  .children 生成器,可以对tag的子节点进行循环
for child in title_tag.children:
    print(child)


# .contents 和 .children 属性仅包含tag的直接子节点.
# 例如,<head>标签只有一个直接子节点<title>
# <title>标签也包含一个子节点:字符串 “The Dormouse’s story”,
# 这种情况下字符串 “The Dormouse’s story”也属于<head>标签的子孙节点.
# .descendants 属性可以对所有tag的子孙节点进行递归循环
for child in head_tag.descendants:
    print(child)

