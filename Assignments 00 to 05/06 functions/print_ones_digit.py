def show_ones_digit(number):
    ones_place = number % 10
    print("The ones digit is", ones_place)

def main():
    user_input = int(input("Enter a number: "))
    show_ones_digit(user_input)

if __name__ == '__main__':
    main()
