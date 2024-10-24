import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

# View all contacts
def view_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("\nNo contacts available.")

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    
    if name in contacts:
        print(f"Editing contact {name}. Leave blank to keep the current information.")
        new_phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        new_email = input(f"Enter new email address (current: {contacts[name]['email']}): ")

        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email

        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

# Main menu for the contact manager
def main_menu():
    contacts = load_contacts()
    
    while True:
        print("\nContact Manager:")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting contact manager.")
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Run the contact manager
if __name__ == "__main__":
    main_menu()
