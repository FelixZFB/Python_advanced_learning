# 搜索文档树
# CSS搜索

from bs4 import BeautifulSoup
import re

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# CSS搜索
print(soup.find_all(class_=re.compile("itl")))

# class的值可以搜索部分，也可以全部写入，下面三个结果一样
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
print(css_soup.find_all("p", class_="body"))
print(css_soup.find_all("p", class_="strikeout"))
print(css_soup.find_all("p", class_="body strikeout"))

