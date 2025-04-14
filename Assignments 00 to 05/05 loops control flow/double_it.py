def main():
    user_input = int(input("Enter a number: "))
    
    current_value = user_input
    
    # Keep doubling the current_value until it reaches 100 or greater
    while current_value < 100:
        # Double the current_value and print it
        current_value *= 2
        print(current_value)

if __name__ == '__main__':
    main()
