import random

# Number of sides on each die to roll
SIDES_ON_DICE = 6

def simulate_dice_roll():
    """
    Simulates rolling two dice and prints their total.
    """
    dice1 = random.randint(1, SIDES_ON_DICE)
    dice2 = random.randint(1, SIDES_ON_DICE)
    total_roll = dice1 + dice2
    print("Total of two dice:", total_roll)

def main():
    initial_value = 10
    print("initial_value in main() starts as: " + str(initial_value))
    simulate_dice_roll()
    simulate_dice_roll()
    simulate_dice_roll()
    print("initial_value in main() is still: " + str(initial_value))

if __name__ == '__main__':
    main()
