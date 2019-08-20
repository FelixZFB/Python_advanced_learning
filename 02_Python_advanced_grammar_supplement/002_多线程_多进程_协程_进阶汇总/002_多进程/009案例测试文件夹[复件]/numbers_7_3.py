# coding=utf-8
# 输入一个数字，并确定是否是10的整数倍

integer = input("Please give me a integer: ")
integer = int(integer)
print(integer)

if integer % 10 == 0:
    print("The number " + str(integer) + " is integer of 10.")
else:
    print("The number " + str(integer) + " isn't integer of 10.")

