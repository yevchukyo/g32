"""hw9_contacts/controllers.py"""
from .helpers import in_dict, full_name
import hw9_contacts.models as m
from tabulate import tabulate

def last_id(contacts: list[dict]) -> int:
    return int(contacts[len(contacts) - 1]['id'])

def add_contact() -> str:
    contact = {}
    contacts = m.get_contacts()




    #Отримуємо та перевіряємо номер телефону
    number = input('Enter Phone Number (12 digits) = ').strip()
    if not number.isdigit() or len(number) != 12:
        print("Invalid phone number format. Please enter a 12-digit number.")
        return "Error number"
    
    if in_dict('Phonenumber', number, contacts):
        print(f"The contact {number} is already in the phonebook")
        return f"Error number"
    
    # Отримуємо та перевіряємо ім'я та прізвище
    first_name = input('Enter First Name = ').strip()
    last_name = input('Enter Last Name = ').strip()
    
    if not first_name.isalpha() or not last_name.isalpha():
        print("Invalid name format. Please enter alphabetic characters only.")
        return "Error name"
    
    if in_dict('First name', first_name, contacts) and in_dict('Last name', last_name, contacts):
        print(f"The contact {full_name(first_name, last_name)} is already in the phonebook")
        return f"Error name"
    
    address = input('Enter Address = ').strip()
    
    if len(contacts) == 0:
        id = 1
    else: id = last_id(contacts)+1
         
    contact = {
        'id': str(id),
        'First name': first_name.title(),
        'Last name': last_name.title(),
        'Phonenumber': number,
        'Address': address
        }
    contacts.append(contact)
    m.save_contacts(contacts)
    return f"Contact added syccessfully"


def all_contacts() -> list[dict]:
    return m.get_contacts()

def lookup_contact(target: str) -> list[dict]:
    contacts = m.get_contacts()
    founded_contacts = []
    for key in list(contacts[0].keys())[0:4]:
        for index, contact in enumerate(contacts):
            if contact[key] == target:
                founded_contacts.append(contact)
    return founded_contacts

def remove_contact(index: int) -> str:
    if index in range(len(m.get_contacts())):
        confirm = input("Are You sure You wish delete this contact? (y|n): ")
        if confirm.lower() in ('yes', 'y'):
            m.get_contacts().pop(index)
            return f"element with {index} deleted successfully"
        else:
            return f"element with {index} not deleted"
    else:
        return f"Error: element with {index} noe exists"

def sort_contacts(order: int) -> list[dict]:
    match order:
        case 1:
            return sorted(m.get_contacts(), key=lambda x: x['First name'])
                    
        case 2:
            return sorted(m.get_contacts(), key=lambda x: x['Last name'])

        case _:
            return m.get_contacts()

def clear_phonebook():
    m.clear_contacts()  # Очищаємо список контактів в базі даних
    print("Phonebook cleared")

def main():
    print(F"This is my file: {__file__} to test Python's execution methods.")
    
    print("The value of __name__ is:", repr(__name__))
    
if __name__ == '__main__':
    main()