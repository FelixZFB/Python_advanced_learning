# 读取HTML文件，进行解析

from lxml import etree

# 打开HTML文件
#指定解析器HTMLParser会根据文件修复HTML文件中缺失的如声明信息
html = etree.parse('./67_3.html', etree.HTMLParser())

#解析成字节
result1 = etree.tostring(html, pretty_print=True)
#解析成列表
result2 = etree.tostringlist(html)


print(type(result1))
print(type(result2))

print(result1)