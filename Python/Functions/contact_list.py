def add_contact(filename):
    """Append a new contact to the file."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    with open(filename, 'a') as f:
        f.write(f"{name}, {phone}\n")
    print(f"Contact {name} added successfully!\n")

def view_contacts(filename):
    """Read and display all contacts."""
    try:
        with open(filename, 'r') as f:
            contacts = f.readlines()
            if not contacts:
                print("No contacts found.\n")
            else:
                print("Contacts:")
                for contact in contacts:
                    name, phone = contact.strip().split(', ')
                    print(f"{name}: {phone}")
                print()
    except FileNotFoundError:
        print("No contacts file found. Add some contacts first.\n")

def search_contact(filename):
    """Search for a contact by name."""
    search_name = input("Enter the name of the contact: ")
    try:
        with open(filename, 'r') as f:
            for line in f:
                name, phone = line.strip().split(', ')
                if name.lower() == search_name.lower():
                    print(f"{name}: {phone}\n")
                    return
            print(f"No contact found with the name {search_name}.\n")
    except FileNotFoundError:
        print("No contacts file found. Add some contacts first.\n")

def main():
    filename = 'contacts.txt'
    while True:
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(filename)
        elif choice == '2':
            view_contacts(filename)
        elif choice == '3':
            search_contact(filename)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()
