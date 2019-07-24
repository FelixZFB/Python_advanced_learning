# coding=utf-8
# 定义一个活动值为True(True 和 False 都需要大写，才能正确识别),如果返回值为True就继续运行，如果为False就停止while循环
# 详细说明参考教材P1057

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        avtive = False
    else:
        print(message)


