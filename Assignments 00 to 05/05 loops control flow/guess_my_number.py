import random

def main():
    secret_number = random.randint(1, 99)
    
    print("🎯 I'm thinking of a number between 1 and 99...")

    user_guess = int(input("Enter your guess: "))

    while user_guess != secret_number:
        if user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        user_guess = int(input("Enter a new guess: "))
    
    print(f"🎉 Congrats! You guessed it right. The number was: {secret_number}")

if __name__ == '__main__':
    main()
