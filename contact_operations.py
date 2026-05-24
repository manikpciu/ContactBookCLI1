# contact_operations.py
import csv
import os

FIELDS = ["Name", "Phone", "Email", "Address"]

def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, newline='', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    return contacts

def save_contacts(contacts, filename="contacts.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

def is_duplicate(contacts, phone):
    for contact in contacts:
        if contact["Phone"] == phone:
            return True
    return False

def add_contact(contacts):
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        if not phone.isdigit():
            raise ValueError("The phone number must be an integer.")
        if is_duplicate(contacts, phone):
            print("Error: Phone number already exists for another contact.")
            return
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        new_contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(new_contact)
        save_contacts(contacts)
        print("Contact added successfully!")
    except ValueError as ve:
        print("Error:", ve)

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("===== All Contacts =====")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name : {contact['Name']}\n   Phone : {contact['Phone']}\n   Email : {contact['Email']}\n   Address: {contact['Address']}\n")
    print("========================")

def search_contact(contacts):
    term = input("Enter search term (name/email/phone): ").lower()
    found = False
    for contact in contacts:
        if term in contact["Name"].lower() or term in contact["Email"].lower() or term in contact["Phone"]:
            print("Search Result:")
            print(f"Name : {contact['Name']}\nPhone : {contact['Phone']}\nEmail : {contact['Email']}\nAddress: {contact['Address']}")
            found = True
            break
    if not found:
        print("No matching contact found.")

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ")
    for contact in contacts:
        if contact["Phone"] == phone:
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    print("Contact with that phone number not found.")
