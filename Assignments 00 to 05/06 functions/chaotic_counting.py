import random

# Likelihood of stopping early
DONE_PROBABILITY = 0.5

# Function that randomly decides whether to stop counting
def should_stop():
    return random.random() < DONE_PROBABILITY

# Function that counts from 1 to 10, but might stop early
def start_counting():
    for number in range(1, 11):
        if should_stop():
            return 
        print(number)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    start_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
