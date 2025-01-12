import random

computer = random.choice([1, 0, -1])

user = input("Enter your choice like 'r' for 'Rock': ").lower()

choices = {"r": 1, "p": 0, "s": -1}
reversed_dict = {1: "Rock", 0: "Paper", -1: "Scissor"}

# Map user input to the corresponding value
if user in choices:
    user = choices[user]

    print(f"You chose {reversed_dict[user]} \nComputer chose {reversed_dict[computer]}")

    if user == computer:
        print("It's a Draw!")
    elif (user == 1 and computer == -1) or (user == -1 and computer == 0) or (user == 0 and computer == 1):
        print("You Won!")
    else:
        print("Oops! You Lost!")
else:
    print("Invalid choice! Please enter 'r', 'p', or 's'.")
