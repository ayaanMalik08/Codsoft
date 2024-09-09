# Contact class to represent a contact's details
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"

# ContactBook class to manage contacts
class ContactBook:
    def __init__(self):
        self.contacts = []

    # Add a new contact
    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.\n")

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts):
                print(f"{i+1}. {contact.name} - {contact.phone}")
        print()

    # Search for a contact by name or phone number
    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if results:
            print(f"\nSearch Results for '{search_term}':")
            for contact in results:
                print(contact)
        else:
            print(f"No contact found with '{search_term}'.\n")

    # Update a contact's details
    def update_contact(self, search_term):
        found_contact = None
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                found_contact = contact
                break

        if found_contact:
            print(f"\nUpdating contact details for '{found_contact.name}'")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")

            if new_name: found_contact.name = new_name
            if new_phone: found_contact.phone = new_phone
            if new_email: found_contact.email = new_email
            if new_address: found_contact.address = new_address

            print(f"Contact '{found_contact.name}' updated successfully.\n")
        else:
            print(f"No contact found with '{search_term}'.\n")

    # Delete a contact by name or phone number
    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully.\n")
                return
        print(f"No contact found with '{search_term}'.\n")

# Main function to run the contact manager
def main():
    contact_book = ContactBook()

    while True:
        print("--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting the Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.\n")

if __name__ == "__main__":
    main()
