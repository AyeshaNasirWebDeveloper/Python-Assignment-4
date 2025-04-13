def calculate_sum(num_list) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    sum_result: int = 0
    for value in num_list:
        sum_result += value
    return sum_result


def main():
    sample_numbers: list[int] = [1, 2, 3, 4, 5]  # Sample list of numbers
    total: int = calculate_sum(sample_numbers)  # Get the total sum
    print("The sum of the numbers is:", total)  # Display the sum


if __name__ == '__main__':
    main()
