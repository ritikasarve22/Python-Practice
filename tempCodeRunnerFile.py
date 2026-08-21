import random

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : ")) 

print(num1,num2,num3)

if num1 == num2 == num3 :
    print("🥳 Jackpot !")
elif num1 == num2 or num2 == num3 or num1 == num3 :
    print("🫶🏻 Small Jackpot")
else :
    print("Better luck next time !!")
     