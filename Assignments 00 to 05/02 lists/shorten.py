MAX_LENGTH = 3  # Define the maximum allowed length for the list

def shorten(items):
    """Removes items from the end of the list until its length is MAX_LENGTH."""
    while len(items) > MAX_LENGTH:
        removed_item = items.pop()  # Remove the last item from the list
        print(removed_item)  # Print the item that was removed

def get_user_input():
    """Prompts the user to enter items into a list until they press enter without typing anything."""
    user_list = []
    item = input("Enter an item (press enter to stop): ")  # Ask for the first input
    while item != "":  # Continue until the user presses enter without typing anything
        user_list.append(item)  # Add the item to the list
        item = input("Enter an item (press enter to stop): ")  # Get the next input
    return user_list

def main():
    items = get_user_input()  # Get the list from the user
    shorten(items)  # Shorten the list if needed

if __name__ == '__main__':
    main()
