# 本案例来自案例43_5,使用的urllib库
# 本案例使用requests库

"""
大致流程：
1. 利用data构造内容
2. 返回一个json格式的内容
3. 结果就应该是girl的释义
"""

# 本案例使用requests,会发现会比43_5案例编码简洁很多
# data直接使用字典，不用编码，json数据可以直接读取也不用解码

import requests

baseurl = 'https://fanyi.baidu.com/sug'

# 存储用来模拟formdata的数据一定是字典格式
wd = input('Input your keyword: ')
data = {'kw': wd}

# 43_5中需要对data进行编码，编码为字节
# data = parse.urlencode(data).encode('utf-8')
# requests中可以直接使用字典格式的data
rsp = requests.post(baseurl, data=data)

# 直接取出json数据就是一个python格式的字典了
json_data = rsp.json()


# 查看结果是一个字典，取出字典中键data对应的值是一个列表，
# 列表中又是有多个字典,每个字典中有两个键值对，将两个值取出，一一对应
for item in json_data['data']:

    print(item['k'], "-----", item['v'])