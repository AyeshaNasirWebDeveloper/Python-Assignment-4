def save_contacts():
    contacts = {}
    while True:
        person_name = input("Name: ")
        if person_name == "":
            break
        phone_number = input("Number: ")
        contacts[person_name] = phone_number
    return contacts

def display_contacts(contacts):
    print("\nSaved Contacts:")
    for person, number in contacts.items():
        print(f"{person} -> {number}")

def search_contact(contacts):
    while True:
        search_name = input("Enter name to lookup: ")
        if search_name == "":
            break
        if search_name in contacts:
            print(f"{search_name}'s number is {contacts[search_name]}")
        else:
            print(f"{search_name} is not in the contact list.")

def main():
    contact_list = save_contacts()
    display_contacts(contact_list)
    search_contact(contact_list)

if __name__ == '__main__':
    main()
