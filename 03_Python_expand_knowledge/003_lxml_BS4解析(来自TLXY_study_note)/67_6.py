#!/usr/bin/env python
# coding:utf-8
import requests
from requests.exceptions import RequestException
from lxml import etree
import json


def one_to_page(html):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    try:
        response = requests.get(html, headers=headers)
        body = response.text  # 获取网页内容
    except RequestException as e:
        print('request is error!', e)
    try:
        html = etree.HTML(body, etree.HTMLParser())  # 解析HTML文本内容
        result = html.xpath('//table[contains(@class,"table-top20")]/tbody/tr//text()')  # 获取列表数据
        pos = 0
        for i in range(20):
            if i == 0:
                yield result[i:5]
            else:
                yield result[pos:pos + 5]  # 返回排名生成器数据
            pos += 5
    except ParseError as e:
        print(e.position)


def write_file(data):  # 将数据重新组合成字典写入文件并输出
    for i in data:
        sul = {
            '2018年6月排行': i[0],
            '2017年6排行': i[1],
            '开发语言': i[2],
            '评级': i[3],
            '变化率': i[4]
        }
        with open('test.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(sul, ensure_ascii=False) + '\n')  # 必须格式化数据
            f.close()
        print(sul)
    return None


def main():
    url = 'https://www.tiobe.com/tiobe-index/'
    data = one_to_page(url)
    revaule = write_file(data)
    if revaule == None:
        print('ok')


if __name__ == '__main__':
    main()

