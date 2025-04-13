def main():
    original_list: list[int] = [1, 2, 3, 4]  # Starting list of numbers

    for index in range(len(original_list)):
        original_list[index] *= 2  # Double each value directly

    print("Doubled list:", original_list)


if __name__ == '__main__':
    main()
