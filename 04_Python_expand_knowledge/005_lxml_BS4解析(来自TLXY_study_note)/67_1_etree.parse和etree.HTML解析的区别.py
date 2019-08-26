# etree.parse，传入的html源文档
# 可以直接传入.html文件直接解析

# etree.HTML，传入的text字符串
# 先获取的html源文档，然后再获取text文档后进行解析


# etree.parse案例
# 打开HTML文件
#指定解析器HTMLParser会根据文件修复HTML文件中缺失的如声明信息
# html = etree.parse('./67_3.html', etree.HTMLParser())


# etree.HTML案例
# 比如：
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
#     }
#     try:
#         response = requests.get(html, headers=headers)
#         body = response.text  # 获取网页内容文档
#     except RequestException as e:
#         print('request is error!', e)
#     try:
#         html = etree.HTML(body, etree.HTMLParser())  # 解析HTML文本内容
#      。。。。。。