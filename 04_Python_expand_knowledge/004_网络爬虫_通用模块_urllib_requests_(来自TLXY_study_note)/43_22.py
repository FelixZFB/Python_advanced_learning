# 利用参数headers和params研究返回的内容
# 研究返回的结果

import  requests

# 完整的访问url是下面的url加上参数组成的完整url
url = 'http://www.baidu.com/s?'

kw = {
    'wd': '美女'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2854.400'
}

rsp = requests.get(url, params=kw, headers=headers)

# print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)



