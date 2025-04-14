def show_divisors(number: int):
    print(f"Here are the divisors of {number}")
    for possible_divisor in range(1, number + 1):
        if number % possible_divisor == 0:
            print(possible_divisor)

def main():
    user_input = int(input("Enter a number: "))
    show_divisors(user_input)

if __name__ == '__main__':
    main()
