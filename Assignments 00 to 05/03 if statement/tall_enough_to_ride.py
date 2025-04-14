MIN_HEIGHT = 50

def main():
    user_height = float(input("How tall are you? "))

    if user_height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
