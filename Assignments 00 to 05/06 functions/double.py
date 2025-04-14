def multiply_by_two(value):
    return value * 2

def main():
    user_input = int(input("Enter a number: "))
    result = multiply_by_two(user_input)
    print("Double that is", result)

if __name__ == '__main__':
    main()
