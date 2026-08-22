''' 🧠 Math Quiz Game
Computer randomly generates two numbers and an operator (+, -, *).
User enters the answer.
Correct → 1 point
Wrong → 0 points'''

import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)

operator = random.choice(["+","-","*"])

score = 0 

if operator == "+" :
    correct_answer = num1 + num2 

elif operator == "-" :
    correct_answer = num1 - num2

else:
    correct_answer = num1 * num2 

print(num1, operator, num2)

answer = int(input("Enter your answer : "))

if answer == correct_answer :
    score = score + 1
    
else :
    print("Wrong Answer !")


print("YOUR SCORE : ", score)
