# coding=utf-8
# 定义一个退出值，输入这个值退出，不是这个值，就一直循环运行
# while首次运行时和空字符串比较，和quit不相等，然后message就等于input函数的输入值，
# prompt两行文字，第一次运行，先打印出来了input函数的内容，后然后输入要输入的值
# message就等于输入的值，同时将这个值打印出来，这个值又和quit比较，如果不相等就继续下个循环。
# 详细说明参考教材P105

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
