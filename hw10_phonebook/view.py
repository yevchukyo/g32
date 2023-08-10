import tabulate
from hw10_phonebook import TITLE
class PhonebookView:
    def display_menu(self):
        print(f"Hi! It's me, Your {TITLE}")
        return input("What You wanna do? [a(dd)|l(ist)|f(ind)|r(emove)|c(lear)|q(uit))]: ")

    def display_contacts(self, contacts):
        if contacts:
            headers = ['id', 'First name', 'Last name', 'Phonenumber', 'Address']
            table = []
            for i, contact in enumerate(contacts):
                table.append([i, contact.first_name, contact.last_name, contact.phone_number, contact.address])
            
            print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid"))
        else:
            print("No results found.")

    def display_search_results(self, contacts):
        print(f"{TITLE} - Search Results")
        if contacts:
            for contact in contacts:
                print(f"Name: {contact.first_name} {contact.last_name}")
                print(f"Phone: {contact.phone_number}")
                print(f"Address: {contact.address}")
                print("=" * 20)
        else:
            print("No results found.")

    def bye(self):
        print(f"Thank You for using {TITLE}")
        exit(0)
