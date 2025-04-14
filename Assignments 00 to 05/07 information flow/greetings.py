def greet_person(name):
    return f"Greetings {name}!"

def main():
    user_name = input("What's your name? ")
    greeting = greet_person(user_name)
    print(greeting)

if __name__ == '__main__':
    main()
