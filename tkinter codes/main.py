phonebook = {}

def add():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    phonebook[name] = phone
    print(f"Contact {name} added successfully!")


def display_all_contacts():
    if phonebook:
        print("\nPhonebook:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Phonebook is empty!")

def menu():
    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add()
        elif choice == '2':
            display_all_contacts()
        elif choice == '3':
            print("Exiting Phonebook...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the phonebook menu
menu()
