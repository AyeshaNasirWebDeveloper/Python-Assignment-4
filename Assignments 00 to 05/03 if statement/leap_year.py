def main():
    entered_year = int(input("Enter a year to check if it's a leap year: "))

    if (entered_year % 4 == 0 and entered_year % 100 != 0) or (entered_year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == '__main__':
    main()
