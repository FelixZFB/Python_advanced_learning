# comment注释对象

from bs4 import BeautifulSoup

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"

soup = BeautifulSoup(markup, 'lxml')

# 查看注释对象中的注释内容
comment = soup.b.string

print(type(comment))  # 特殊对象 注释  <class 'bs4.element.Comment'>
print(comment)

