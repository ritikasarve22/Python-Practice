'''🎰 Lucky Slot Game
Computer generates 3 random numbers from 1–5.

All same → Jackpot 🎉
Two same → Small Win
All different → Try Again'''

import random

num1 = random.randint(1,5)
num2 = random.randint(1,5)
num3 = random.randint(1,5) 

print(num1,num2,num3)

if num1 == num2 == num3 :
    print("🥳 Jackpot !")
elif num1 == num2 or num2 == num3 or num1 == num3 :
    print("🫶🏻 Small Jackpot")
else :
    print("Better luck next time !!")
     