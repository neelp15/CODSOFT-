class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone, email, address))
        print(f"Contact for {name} added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.\n")
            return

        print("Contact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name} - {contact.phone}")
        print()

    def search_contact(self):
        query = input("Enter name or phone number to search: ")
        results = [c for c in self.contacts if query.lower() in c.name.lower() or query in c.phone]
        if results:
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No contacts found matching the query.\n")

    def update_contact(self):
        query = input("Enter the name of the contact to update: ")
        for contact in self.contacts:
            if contact.name.lower() == query.lower():
                print(f"Updating details for {contact.name}:")
                contact.name = input(f"New name (current: {contact.name}): ") or contact.name
                contact.phone = input(f"New phone (current: {contact.phone}): ") or contact.phone
                contact.email = input(f"New email (current: {contact.email}): ") or contact.email
                contact.address = input(f"New address (current: {contact.address}): ") or contact.address
                print("Contact updated successfully!\n")
                return
        print("Contact not found.\n")

    def delete_contact(self):
        query = input("Enter the name of the contact to delete: ")
        for contact in self.contacts:
            if contact.name.lower() == query.lower():
                self.contacts.remove(contact)
                print(f"Contact for {contact.name} deleted successfully!\n")
                return
        print("Contact not found.\n")

    def run(self):
        while True:
            print("Menu:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting the Contact Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

# Run the Contact Manager
if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
