'''🎲 Dice Game 
The computer rolls a dice with a number between 1 and 6. The user also enters a number.
Same number → You Win 🎉
Different number → Computer Wins 🤖'''

import random

choices = [1,2,3,4,5,6]

computer = random.choice(choices)

user = int(input("Enter your choice = 1,2,3,4,5 or 6 : "))

print("Computer choice :  ",computer)

if user == computer :
    print("You Win!")
else:
    print("Computer Wins!")
