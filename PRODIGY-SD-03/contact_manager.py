
import json
import os

CONTACTS_FILE = "contacts.json"

# ---------- Utility Functions ----------

def load_contacts():
    """Load contacts from file if available."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_contacts(contacts):
    """Save contacts to file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def show_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("\n📭 No contacts found.")
        return
    print("\n📒 Contact List:")
    print("-" * 50)
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("-" * 50)

# ---------- CRUD Operations ----------

def add_contact(contacts):
    print("\n➕ Add New Contact")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")

def edit_contact(contacts):
    show_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if index < 0 or index >= len(contacts):
            print("⚠️ Invalid index.")
            return
        contact = contacts[index]
        print("\nLeave field empty to keep current value.")
        new_name = input(f"Name ({contact['name']}): ").strip() or contact['name']
        new_phone = input(f"Phone ({contact['phone']}): ").strip() or contact['phone']
        new_email = input(f"Email ({contact['email']}): ").strip() or contact['email']
        contacts[index] = {"name": new_name, "phone": new_phone, "email": new_email}
        save_contacts(contacts)
        print("✅ Contact updated successfully!")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_contact(contacts):
    show_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("⚠️ Invalid index.")
            return
        deleted = contacts.pop(index)
        save_contacts(contacts)
        print(f"🗑️ Contact '{deleted['name']}' deleted successfully!")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# ---------- Main Menu ----------

def main():
    contacts = load_contacts()
    while True:
        print("\n===  Contact Management System ===")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("💾 Saving contacts and exiting... Goodbye!")
            save_contacts(contacts)
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
