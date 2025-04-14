def main():
    affirmation = "I am capable of doing anything I put my mind to."
    
    print(f"Please type the following affirmation: {affirmation}")

    user_input = input()  

    # Keep asking until the user types the affirmation correctly
    while user_input != affirmation:
        print("That was not the affirmation.")  
        print(f"Please type the following affirmation: {affirmation}")
        user_input = input() 

    print("That's right! :)")

if __name__ == '__main__':
    main()
