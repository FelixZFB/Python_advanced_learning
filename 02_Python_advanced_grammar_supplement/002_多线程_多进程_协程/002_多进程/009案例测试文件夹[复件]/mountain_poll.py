# coding=utf-8
# 采用while循环来输入一个调查列表，并且存储到字典中
# 详细说明见书P112

responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # 将答卷存储到字典中
    responses[name] = response
    
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let anothor person respond? (Yes/No) ")
    if repeat == 'No':
        polling_active = False

# 调查结束，显示调查结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
