# coding=utf-8
# Á·Ï°whileºÍinputº¯Êý

prompt = "\nWhat matarials do you want to add in pizza?"
prompt += "\nEnter 'quit' to end the program. "

message = " "
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("Ok, we will add " + message + " in your pizza.")
