def main():
    values = []  # Create an empty list to store user inputs

    user_input = input("Enter a value: ")  # Ask the user for the first input
    while user_input:  # Continue if the input is not empty
        values.append(user_input)  # Add the input value to the list
        user_input = input("Enter a value: ")  # Ask for the next value

    print("Here's the list:", values)  # Print the list once the user presses enter without typing anything

if __name__ == '__main__':
    main()
