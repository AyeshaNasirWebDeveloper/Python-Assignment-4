def repeat_message(text: str, times: int):
    for _ in range(times):
        print(text)

def main():
    user_message = input("Please type a message: ")
    repeat_count = int(input("Enter a number of times to repeat your message: "))
    repeat_message(user_message, repeat_count)

if __name__ == '__main__':
    main()
