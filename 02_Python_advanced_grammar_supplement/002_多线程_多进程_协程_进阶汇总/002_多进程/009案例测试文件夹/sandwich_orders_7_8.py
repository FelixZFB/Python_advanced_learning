# coding=utf-8
# 创建一个三明治列表
# 详细说明见书P113

sandwish_orders = ['beef', 'banana', 'apple']
finished_sandwiches = []

while sandwish_orders:
    current_sandwiche = sandwish_orders.pop()
    print("I made your " + current_sandwiche + " sandwish")
    finished_sandwiches.append(current_sandwiche)

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
