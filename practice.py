'''import random

choices = ["stone", "paper", "scissors"]

computer = random.choice(choices)
user = input("Enter stone, paper or scissors: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("Draw! 🤝")

elif user == "stone" and computer == "scissors":
    print("You Win! 🎉")

elif user == "paper" and computer == "stone":
    print("You Win! 🎉")

elif user == "scissors" and computer == "paper":
    print("You Win! 🎉")

else:
    print("Computer Wins! 🤖")'''

# Stone Paper Scissor Game 
import random

choices = ["stone" , "paper" , "scissor"]

computer = random.choice(choices)

user = input("Enter stone , paper or scissor :  ")

print("Computer choice : ",computer)

if user == computer :
    print("draw🫱🏻‍🫲🏻")

elif user == "stone" and computer == "paper":
    print("Computer Wins !")

elif user == "paper" and computer == "stone":
    print("You Win !")

elif user == "paper" and computer == "scissor":
    print("Computer Wins !")

elif user == "scissor" and computer == "paper":
    print("You Wins !")

elif user == "stone" and computer == "scissor":
    print("You Wins !")

else:
    print("Computer Wins ! ")


