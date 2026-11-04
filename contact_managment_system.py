# ==============================================================
#               CONTACT MANAGEMENT SYSTEM
# ==============================================================

# Student Name          : Mansu Ram Garai
# ERP ID                : RU-26-01262
# Course                : BCA
# Programming Language  : Python 3
# Project Number        : PS No. 03
# Project Description   : Created a contact book application that supports Create, Read, 
#                         Update, Delete (CRUD) operations on contacts with search by name. 
# =============================================================
contacts = []

def add_contact(name, phone, email=""):
    name = name.strip()
    phone = str(phone).strip()
    email = str(email).strip()

    # Validation: exactly 10 digits
    if not (phone.isdigit() and len(phone) == 10):
        print("Invalid phone number. Enter exactly 10 digits.")
        return False

    # Duplicate check
    
    for c in contacts:
        if c['phone'] == phone:
            print("Contact with this number already exists.")
            return False

    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact added: {name} | {phone}")
    return True

def search_contact(query):
    query = query.strip().lower()
    found = False
    for c in contacts:
        if query in c['name'].lower():
            if c['email']:
                print(f"{c['name']} | {c['phone']} | {c['email']}")
            else:
                print(f"{c['name']} | {c['phone']}")
            found = True
    if not found:
        print("Contact not found.")
    return found

def update_contact(name, new_phone):
    name = name.strip()
    new_phone = str(new_phone).strip()
    
    if not (new_phone.isdigit() and len(new_phone) == 10):
        print("Invalid phone number. Enter exactly 10 digits.")
        return False

    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = new_phone
            print(f"Phone updated: {new_phone}")
            return True
    print("Contact not found.")
    return False

def delete_contact(name):
    global contacts
    name = name.strip()
    initial_len = len(contacts)
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    
    if len(contacts) < initial_len:
        print(f"Contact '{name}' deleted. Total contacts: {len(contacts)}")
        return True
    else:
        print("Contact not found.")
        return False

def view_contacts():
    if not contacts:
        print("No contacts found.")
    for c in contacts:
        if c['email']:
            print(f"{c['name']} | {c['phone']} | {c['email']}")
        else:
            print(f"{c['name']} | {c['phone']}")

# --- Main Menu Loop ---
def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Supports both: "Ravi Sharma, 9876543210, ravi@mail.com" or separate prompts
            data = input("Enter Name, Phone, Email (comma separated): ").strip()
            if ',' in data:
                parts = [p.strip() for p in data.split(',')]
                name = parts[0] if len(parts) > 0 else ""
                phone = parts[1] if len(parts) > 1 else ""
                email = parts[2] if len(parts) > 2 else ""
            else:
                name = data
                phone = input("Enter Phone: ").strip()
                email = input("Enter Email: ").strip()
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            query = input("Enter name to search: ").strip()
            search_contact(query)

        elif choice == '4':
            name = input("Enter name to update: ").strip()
            new_phone = input("Enter new phone: ").strip()
            update_contact(name, new_phone)

        elif choice == '5':
            name = input("Enter name to delete: ").strip()
            delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()