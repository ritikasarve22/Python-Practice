# 🤷🏻‍♀️Number Guessing Game 

import random

number = random.randint(1, 10)

user = int(input("Guess a number between 1 and 10: "))

if user == number:
    print("Correct! 🎉")

elif user > number:
    print("Too high! ⬆️")

else:
    print("Too low! ⬇️")

print("Computer number:", number)