class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email}, {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Add a new contact to the contact book."""
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def view_contacts(self):
        """Display all contacts in the contact book."""
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact}")

    def search_contact(self, query):
        """Search for contacts by name or phone number."""
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        return results

    def update_contact(self, index, new_contact):
        """Update an existing contact."""
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            print(f"Contact '{new_contact.name}' updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        """Delete a contact from the contact book."""
        if 0 <= index < len(self.contacts):
            deleted = self.contacts.pop(index)
            print(f"Contact '{deleted.name}' deleted successfully!")
        else:
            print("Invalid contact index.")

def get_contact_details():
    """Prompt the user for contact details and return a new Contact object."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone, email, address)

def main():
    """Main function to run the contact book application."""
    book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact = get_contact_details()
            book.add_contact(contact)

        elif choice == '2':
            book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = book.search_contact(query)
            if results:
                print("\nSearch Results:")
                for i, contact in enumerate(results, 1):
                    print(f"{i}. {contact}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            book.view_contacts()
            try:
                index = int(input("Enter the number of the contact to update: ")) - 1
                if 0 <= index < len(book.contacts):
                    new_contact = get_contact_details()
                    book.update_contact(index, new_contact)
                else:
                    print("Invalid contact number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            book.view_contacts()
            try:
                index = int(input("Enter the number of the contact to delete: ")) - 1
                book.delete_contact(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '6':
            print("Thank you for using the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()