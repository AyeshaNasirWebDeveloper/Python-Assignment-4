import random

def main():
    total_numbers = 10
    min_number = 1
    max_number = 100

    for _ in range(total_numbers):
        random_num = random.randint(min_number, max_number)
        print(random_num)

if __name__ == '__main__':
    main()
