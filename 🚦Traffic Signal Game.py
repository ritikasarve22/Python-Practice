'''User enters red, yellow, or green.
red → Stop 🛑
yellow → Wait ⚠️
green → Go 🟢'''

import random 

choices = ["red" , "yellow" , "green"]

computer = random.choice(choices)

user = input("Enter you choice (red/yellow/green) :  ")
print("Computer Choice :")

if user == "red":
    print("Stop 🛑")
elif user == "yellow":
    print("Wait ⚠️")
else:
    print("Go 🟢")
