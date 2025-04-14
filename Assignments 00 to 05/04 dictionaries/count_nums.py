def get_numbers_from_user():
    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        numbers.append(int(user_input))
    return numbers

def count_number_frequency(numbers_list):
    frequency = {}
    for number in numbers_list:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return frequency

def show_counts(frequency_dict):
    for number, count in frequency_dict.items():
        print(f"{number} appears {count} times.")

def main():
    user_numbers = get_numbers_from_user()
    number_counts = count_number_frequency(user_numbers)
    show_counts(number_counts)

if __name__ == '__main__':
    main()
