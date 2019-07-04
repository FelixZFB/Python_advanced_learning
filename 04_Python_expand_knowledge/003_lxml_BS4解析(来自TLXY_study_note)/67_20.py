# 搜索文档树
# 定义一个方法搜索


from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# 如果包含 class 属性却不包含 id 属性,那么将返回 True
# 将True传入find_all
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

result = soup.find_all(has_class_but_no_id)
print(result)
