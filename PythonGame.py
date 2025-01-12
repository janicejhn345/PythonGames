import random

# The computer randomly selects between Snake (1), Water (-1), or Gun (0)
computer = random.choice([1, 0, -1])

# User input for their choice (s = Snake, w = Water, g = Gun)
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

# Dictionary mapping user input to respective values (1 for Snake, -1 for Water, 0 for Gun)
youDict = {"s": 1, "w": -1, "g": 0}

# Dictionary to map the values back to names (1 = Snake, -1 = Water, 0 = Gun)
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get the user's choice using the dictionary (you can assume the user inputs valid choices)
you = youDict[youstr]

# Display what both the user and the computer chose
print(f"You chose {reverseDict[you]} and Computer chose {reverseDict[computer]}")

# Check for a draw
if you == computer:
    print("It's a Draw!")
# Checking for the user's winning conditions
elif (you == 1 and computer == -1) or (you == 0 and computer == 1) or (you == -1 and computer == 0):
    print("You Win!!")
# If neither a draw nor a win, the user loses
else:
    print("You Lost!")

    