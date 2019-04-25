# 字符串和列表的转换

l1 = ['a', 1, 'b', 2]
l2 = [str(i) for i in l1]
print(l2)
l3= ''.join(l2)
print(l3)
l4 = list(l3)
print(l4)

# 用网址最后几位编号作为图片的名称
root_url = 'https://b.porngals4.com/media/galleries/1/16/83073-1479192302/abella-danger-karlee-grey-the-seduction-of-abella-danger-5493431-2781391748.jpg'
l = list(root_url)
filename = ''.join(l[-14:])
print(filename)
