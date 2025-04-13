def add_message_to_list(message_list, message):
    for _ in range(3):  # Add the message 3 times
        message_list.append(message)

def main():
    user_message = input("Enter a message to copy: ")  # Get user input
    empty_list = []  # Create an empty list
    print("List before:", empty_list)  # Print list before adding messages
    add_message_to_list(empty_list, user_message)  # Add 3 copies of the message
    print("List after:", empty_list)  # Print list after adding messages

if __name__ == "__main__":
    main()
