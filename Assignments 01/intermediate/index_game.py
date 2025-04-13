def access_element(lst, index):
    """Returns the element at the specified index."""
    if index < 0 or index >= len(lst):
        return "❌ Index out of range."
    return f"✅ Element at index {index}: {lst[index]}"

def modify_element(lst, index, new_value):
    """Replaces the element at the specified index with the new value."""
    if index < 0 or index >= len(lst):
        return "❌ Index out of range."
    old_value = lst[index]
    lst[index] = new_value
    return f"✅ Replaced '{old_value}' with '{new_value}' at index {index}."

def slice_list(lst, start_index, end_index):
    """Returns a new list containing elements from start_index to end_index (exclusive)."""
    if start_index < 0 or end_index > len(lst) or start_index >= end_index:
        return "❌ Invalid slice indices."
    return f"✅ Sliced list: {lst[start_index:end_index]}"

def index_game():
    
    my_list = ['apple', 'mango', 'banana', 'coconut', 'grapes']

    print("🎮 Welcome to the Index Game!")
    print("Your list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1️⃣ Access an element")
        print("2️⃣ Modify an element")
        print("3️⃣ Slice the list")
        print("4️⃣ Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            try:
                index = int(input("Enter index to access: "))
                result = access_element(my_list, index)
                print(result)
            except ValueError:
                print("⚠️ Please enter a valid integer.")

        elif choice == '2':
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                result = modify_element(my_list, index, new_value)
                print(result)
                print("🔄 Updated List:", my_list)
            except ValueError:
                print("⚠️ Please enter valid inputs.")

        elif choice == '3':
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                result = slice_list(my_list, start, end)
                print(result)
            except ValueError:
                print("⚠️ Please enter valid integer indices.")

        elif choice == '4':
            print("\n \n👋 Exiting the game. Thank you for playing!")
            break

        else:
            print("⚠️ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    index_game()