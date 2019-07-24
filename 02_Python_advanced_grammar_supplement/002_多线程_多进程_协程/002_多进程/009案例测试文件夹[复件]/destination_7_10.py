# coding=utf-8
# 调查列表，被调查人的名字，想去的旅行目的地
# 详细说明见书P113

# 首先创建一个空字典用于存储调查结果
responses = {}

prompt_1 = "What's your name? "
prompt_2 = "Where would you want to go? "

active = True
while active:
    name = input(prompt_1)
    destination = input(prompt_2)
    responses[name] = destination
    repeat = input("Would you like to let anothor person respond? (Yes/No) ")
    if repeat == 'No':
        active = False
        
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to go to " + response.title() + ".")

