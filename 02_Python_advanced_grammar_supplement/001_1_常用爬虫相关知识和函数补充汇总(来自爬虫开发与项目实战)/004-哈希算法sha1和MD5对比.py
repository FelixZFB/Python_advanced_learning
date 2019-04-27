# -*- coding: utf-8 -*-

# md5生成一个128bit的结果，通常用32位的16进制字符串表示
# sha1生成一个160bit的结果，通常用40位的16进制字符串表示
# SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长

import hashlib

sha1 = hashlib.sha1()
text1 = 'python hashlib?'
sha1.update(text1.encode('utf-8'))
text1_sha1 = sha1.hexdigest()
print(text1_sha1)

md5 = hashlib.md5()
text2 = 'python hashlib?'
md5.update(text2.encode('utf-8'))
text2_md5 = md5.hexdigest()
print(text2_md5)