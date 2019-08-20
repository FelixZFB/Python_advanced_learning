# coding=utf-8
# 判断一个数是奇数还是偶数

number = input("How tall are you, in inches? ")
number = int(number)
print(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
