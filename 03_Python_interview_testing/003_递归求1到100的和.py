# 定义一个函数 sum_numbers
# 能够接收一个 num 的整数参数
# 计算 1 + 2 + ... num 的结果


def sum_numbers(num):

    # 1. 出口
    if num == 1:
        return 1

    # 2. 数字的累加 num + (1...num -1)
    # 假设 sum_numbers 能够正确的处理 1...num - 1
    temp = sum_numbers(num - 1)

    # 两个数字的相加
    return num + temp


result = sum_numbers(100)
print(result)

# 1. 传入数字100，temp=sum_numbers(99)
# 2. 函数返回值就是100+sum_numbers(99)
# 3. sum_numbers(99)继续调用原函数，返回值就是99+sum_numbers(98)
# 4. ----不断调用
# 5. sum_numbers(2)=2+sum_numbers(1)
# 6. 最终返回：100+99+98+......+2+sum_numbers(1)
# 7. 传入参数为1时候，返回1，退出调用