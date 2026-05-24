# contact_book_main.py
from contact_operations import *

def main():
    contacts = load_contacts("contacts.csv")
    print("Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... Done!\n")

    while True:
        print("=========== MENU ===========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        print("============================")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            remove_contact(contacts)
        elif choice == '5':
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
