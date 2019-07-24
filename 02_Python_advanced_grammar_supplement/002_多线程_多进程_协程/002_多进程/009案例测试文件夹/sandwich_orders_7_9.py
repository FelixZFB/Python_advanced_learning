# coding=utf-8
# 创建一个三明治列表,里面的烟熏牛肉都卖完了
# 详细说明见书P113

sandwish_orders = ['beef', 'pastrami', 'banana', 'pastrami', 'apple', 
    'pastrami',]
print("Pastrami has been sale out.")

# 循环删除所有的partrami
while 'pastrami' in sandwish_orders:
    sandwish_orders.remove('pastrami')

print(sandwish_orders)
