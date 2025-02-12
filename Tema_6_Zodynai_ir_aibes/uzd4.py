# Telefonų knyga

contact_book = {}

# add a new contact
def add_contact():
    contact_name = input("Enter contact name: ")
    
    try:
        contact_number =int(input("Enter contact's phone number: "))
    except ValueError:
        print("Contact is not added! Invalid phone number! ")
        return

    contact_book[contact_name] = contact_number
    print("Contact is added!")
    print(contact_book)

# remove existing contact
def remove_contact():
    contact_name = input("Enter a contact you want to remove: ")
    if contact_book.get(contact_name):
        contact_book.pop(contact_name)
        print(f"Contact is removed! ")
        print(contact_book)
    else:
        print("Contact is not in the book!")

# search for existing contact
def search_contact():
    contact_name = input("Enter a contact you want to search: ")
    if contact_book.get(contact_name):
        contact_index = contact_book[contact_name]
        print(f"Contact is found! Phone number: {contact_index}")
    else:
        print("Contact is not in the book!")


while True:

    menu_selection = input("Contact Book | Select from menu by typing:\n| search | add | remove | quit | ").lower()
    if menu_selection == "quit":
        break
    elif menu_selection == "add":
        add_contact()
    elif menu_selection == "search":
        search_contact()
    elif menu_selection == "remove":
        remove_contact()
    else:
        print("Invalid selection!")


