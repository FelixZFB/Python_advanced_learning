# 遍历文档树
# 子孙节点信息
# string实例

from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

head_tag = soup.head
title_tag = head_tag.contents[0]
print(head_tag)
print(title_tag)

# title标签下只有一个 NavigableString（字符串对象）类型子节点
print(title_tag.string)

# 一个tag仅有一个tag(标签对象)子节点,那么这个tag也可以使用 .string 方法
print(head_tag.string)

# 如果tag包含了多个子节点,tag就无法确定
# .string 方法应该调用哪个子节点的内容,的输出结果是 None
print(soup.html.string)



