def is_within_range(number, lower_bound, upper_bound):
    """
    Returns True if number is between lower_bound and upper_bound, inclusive.
    upper_bound is guaranteed to be greater than lower_bound.
    """
    return lower_bound <= number <= upper_bound

def main():
    # Example usage
    print(is_within_range(5, 1, 10))  # True
    print(is_within_range(15, 1, 10))  # False

if __name__ == '__main__':
    main()
