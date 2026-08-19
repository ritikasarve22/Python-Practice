import random

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
    print("Computer Wins! 🤖")