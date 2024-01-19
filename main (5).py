contacts = []


def add_contact():

  contact = {}
  contact["name"] = input("Enter your name: ")
  contact["phone_number"] = input("Enter your phone number: ")
  contact["email"] = input("Enter your email: ")
  contact["address"] = input("Enter your address: ")
  contacts.append(contact)
  print("Contact added successfully!")


def search_contact():

  name = input("Enter the name to search: ")
  found = False
  for contact in contacts:
    if contact["name"].lower() == name.lower():
      print("Name:", contact["name"])
      print("Phone Number:", contact["phone_number"])
      print("Email:", contact["email"])
      print("Address:", contact["address"])
      found = True
      break
  if not found:
    print("Contact not found.")


def display_contacts():

  if not contacts:
    print("No contacts in the list.")
  else:
    print("Contacts:")
    for contact in contacts:
      print("-" * 20)
      print("Name:", contact["name"])
      print("Phone Number:", contact["phone_number"])
      print("Email:", contact["email"])
      print("Address:", contact["address"])


while True:
  print("\nContact Book Menu:")
  print("1. Add Contact")
  print("2. Search Contact")
  print("3. Display All Contacts")
  print("4. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    add_contact()
  elif choice == "2":
    search_contact()
  elif choice == "3":
    display_contacts()
  elif choice == "4":
    break
  else:
    print("Incorrect choice.")
