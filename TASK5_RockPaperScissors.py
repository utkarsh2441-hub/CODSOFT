import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    print("\n__ROCK PAPER SCISSORS__")

    user = input("Enter Rock, Paper or Scissors: ").lower()

    if user not in choices:
        print("Invalid Choice!")
        continue

    computer = random.choice(choices)

    print("You Chose:", user)
    print("Computer Chose:", computer)

    if user == computer:
        print("Match Draw!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print("You      :", user_score)
    print("Computer :", computer_score)

    play_again = input("\nPlay Again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("You      :", user_score)
        print("Computer :", computer_score)
        print("Thanks for Playing!")
        break