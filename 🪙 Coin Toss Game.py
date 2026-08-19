''' 🪙 Coin Toss Game
Computer randomly chooses "head" or "tail". User makes a guess.
Same → You Win
Different → Computer Wins'''

import random

choices = ["head" or "tail"]

computer = random.choice(choices)

user = input("Enter your choice  (head / tail) :")
print("Computer choice : ",computer)

if user == computer :
    print("You Win !")
else:
    print("Computer Wins !")
