# 遍历文档树
# 子孙节点信息

from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# .contents 属性可以将tag的所有子节点以列表的方式输出
# 取出title标签
head_tag = soup.head
print(head_tag.contents)
print(head_tag.contents[1])
print('*' * 50)


# 取出title标签
title_tag = head_tag.contents[1]
print(title_tag)
print(title_tag.contents) # title的子节点就是标签里面的内容

# soup下面也有子节点HTML
print(len(soup.contents))
print(soup.contents[0].name)
print('*' * 50)


#  .children 生成器,可以对tag的子节点进行循环
for child in title_tag.children:
    print(child)
print('*' * 50)

# .contents 和 .children 属性仅包含tag的直接子节点
# 注意：如果有换行符，也会识别为一个子节点\n
# 例如,<head>标签只有一个直接子节点<title>
# <title>标签也包含一个子节点:字符串 “The Dormouse’s story”,
# 这种情况下字符串 “The Dormouse’s story”也属于<head>标签的子孙节点.
# .descendants 属性可以对所有tag的子孙节点进行递归循环
for child in head_tag.descendants:
    print(child)
print('*' * 50)

# <title>The Dormouse's story</title>是子节点
# The Dormouse's story是孙节点