# 标签中内容不能编辑，但是可以替换

from bs4 import BeautifulSoup

html = '<b class="boldest">Extremely bold</b>'

soup = BeautifulSoup(html, 'lxml')

print(soup)
print(soup.b.string)

# 标签中的内容可以替换
soup.b.string.replace_with('No longer bold')
print(soup)

