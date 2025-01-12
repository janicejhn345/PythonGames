import random
import time

# Initialize score
score = 0

# Run the game for a certain number of rounds (for example, 5 rounds)
for round_num in range(5):
    # Generate random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Choose a random operator
    operator = random.choice(['+', '-', '*'])

    # Create the problem
    problem = f"{num1} {operator} {num2}"

    # Calculate the correct answer
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    # Start the timer
    start_time = time.time()

    # Ask the player for their answer
    try:
        player_answer = int(input(f"Solve this problem: {problem} = "))
    except ValueError:
        player_answer = None

    # Calculate time taken to answer
    time_taken = time.time() - start_time

    # Check if the time is within the limit (e.g., 5 seconds)
    if time_taken > 5:
        print("Time's up! You took too long to answer.")
    elif player_answer == correct_answer:
        print("Correct! You earn a point!")
        score += 1  # Increase score
    else:
        print(f"Oops! The correct answer was {correct_answer}.")

# Show final score
print(f"\nGame over! Your final score is: {score} out of 5.")







