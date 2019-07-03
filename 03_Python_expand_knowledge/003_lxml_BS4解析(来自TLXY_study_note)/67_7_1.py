# coding: utf-8
# 提取网络爬虫百科词条中，词条摘要中相关词条的连接

import re
from bs4 import BeautifulSoup
import requests

url = 'https://baike.baidu.com/item/网络爬虫/5162711?fr=aladdin'
# url = 'https://www.baidu.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers = {'User-Agent': user_agent}
        # 请求获取网址
r = requests.get(url, headers=headers)
r.encoding = 'utf-8' # 解决中文乱码的问题
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')

# 方法1：使用正则提取代码中部分a标签
links = soup.find_all('a', href=re.compile(r'/item/%E8%9'))
# links = soup.select(".lemma-summary a::attr(href)").extract_first()
print(len(links))
print(links)
for link in links:
    # 提取href的属性，既URL地址
    new_url = link['href']
    print(new_url)
print('\n')

# 方法2：查找唯一的一个标签
title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
print(title)
print(title.get_text())
print('\n')
summary = soup.find('div', class_='lemma-summary')
print(summary.get_text())

# 方法3：查找唯一的标签，然后找出里面所有的a标签，提取a标签的连接属性
links = soup.find('div', class_='lemma-summary').find_all('a')
print(links)
for link in links:
    # 提取href的属性，既URL地址
    new_url = link['href']
    print(new_url)

# 方法4，使用CSS选择器，但是查找a标签会提示伪类错误





