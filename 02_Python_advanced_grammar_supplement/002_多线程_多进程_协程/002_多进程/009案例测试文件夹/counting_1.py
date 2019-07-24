# coding=utf-8
# 使用continue函数，返回循环开头，如果不满足条件，运行剩余的代码

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)
   
