# 搜索文档树


from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# 找到文档中所有<a>标签和<b>标签
print(soup.find_all(['a','b']))
print("*" * 50)

# True 可以匹配任何值的标签，即返回所有标签
# 实际返回的是一个包含html文档内容的列表
print(soup.find_all(True))
print("*" * 50)


# 遍历取出所有标签的name，但是不会返回字符串节点
for tag in soup.find_all(True):
    print(tag.name)
print("*" * 50)