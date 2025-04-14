def is_odd_number(number: int):
    return number % 2 == 1

def main():
    for current_number in range(10, 20):
        if is_odd_number(current_number):
            print(f"{current_number} odd")
        else:
            print(f"{current_number} even")

if __name__ == '__main__':
    main()
