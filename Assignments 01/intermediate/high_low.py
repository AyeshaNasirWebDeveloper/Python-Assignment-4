import random

NUM_ROUNDS = 5
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0  # player's score

    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}")

        # Generate random numbers for player and computer
        user_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)

        print(f"Your number is {user_number}")

        # Get user input and validate it
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either higher or lower: ").lower()

        # Game logic
        if user_number > computer_number and guess == "higher":
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif user_number < computer_number and guess == "lower":
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")

    # Game over message
    print("Thanks for playing!")

    # Final performance message
    if score == NUM_ROUNDS:
        print("\nWow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("\nGood job, you played really well!")
    else:
        print("\nBetter luck next time!")

if __name__ == '__main__':
    main()