def print_first_element(elements):
    
    print(elements[0])

def collect_elements():
    elements = []
    user_input = input("Enter an element or press enter to stop: ")
    while user_input != "":
        elements.append(user_input)
        user_input = input("Enter an element or press enter to stop: ")
    return elements

def main():
    user_elements = collect_elements()  # Collects elements from the user
    print_first_element(user_elements)  # Prints the first element of the list

if __name__ == '__main__':
    main()
