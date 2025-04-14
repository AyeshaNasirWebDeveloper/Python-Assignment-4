def count_even_numbers(numbers):
    """
    Prints the number of even numbers in the list.
    """
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    print("Number of even numbers:", even_count)

def get_numbers_from_user():
    """
    Asks the user to enter numbers until they press Enter.
    Returns a list of entered numbers.
    """
    number_list = []
    user_input = input("Enter an integer or press enter to stop: ")
    
    while user_input != "":
        number = int(user_input)
        number_list.append(number)
        user_input = input("Enter an integer or press enter to stop: ")
    
    return number_list

def main():
    user_numbers = get_numbers_from_user()
    count_even_numbers(user_numbers)

if __name__ == '__main__':
    main()
