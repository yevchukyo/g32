import re
import typer
from hw10_phonebook.model import Phonebook, Contact
from hw10_phonebook.view import PhonebookView

app = typer.Typer()

class PhonebookController:
    def __init__(self, data_file):
        self.phonebook = Phonebook(data_file)
        self.view = PhonebookView()

    def find_contact(self, search_query):
        found_contacts = []
        pattern = re.compile(re.escape(search_query), re.IGNORECASE)
        
        for contact in self.phonebook.contacts:
            if any(pattern.search(value) for value in [contact.first_name, contact.last_name, contact.phone_number, contact.address]):
                found_contacts.append(contact)
        
        return found_contacts

    def run(self):
        while True:
            command = self.view.display_menu()

            if command in ('a', 'add'):
                self.add_contact()
            elif command in ('f', 'find'):
                search_query = typer.prompt("Enter search query: ").strip().lower()
                found_contacts = self.find_contact(search_query)
                self.view.display_search_results(found_contacts)
            elif command in ('l', 'list'):
                order = typer.prompt("Enter order by name = 1 or order by surname = 2: ")
                while not order.isdigit():
                    typer.echo("Invalid input. Please enter a valid option.")
                    order = typer.prompt("Enter order by name = 1 or order by surname = 2: ")

                order = int(order)
                if order == 1:
                    sortedbook = sorted(self.phonebook.contacts, key=lambda x: x.first_name)
                    self.view.display_contacts(sortedbook)
                elif order == 2:
                    sortedbook = sorted(self.phonebook.contacts, key=lambda x: x.last_name)
                    self.view.display_contacts(sortedbook)
                else:
                    typer.echo('Contact list not sorted')
                    sortedbook = self.phonebook.contacts
                    self.view.display_contacts(sortedbook)
            elif command in ('r', 'remove', 'delete'):
                index = typer.prompt("What contact You wanna remove? :")
                if index.isdigit():
                    index = int(index)
                    if index in range(len(self.phonebook.contacts)):
                        confirm = typer.prompt("Are You sure You wish to delete this contact? (y|n): ")
                        if confirm.lower() in ('yes', 'y'):
                            self.phonebook.contacts.pop(index)
                            self.phonebook.save_data()
                            self.view.display_contacts(self.phonebook.contacts)
                        else:
                            continue
                    else:
                        typer.echo(f"Error: element with index {index} does not exist")
                else:
                    typer.echo("Invalid input. Please enter a valid option.")
            elif command in ('c', 'clear'):
                confirm = typer.prompt("Are You sure You wish to clear the phonebook? (y|n): ")
                if confirm.lower() in ('yes', 'y'):
                    self.phonebook.contacts.clear()
                    self.phonebook.save_data()
                    typer.echo("Phonebook cleared")
                    self.view.display_contacts(self.phonebook.contacts)
            elif command in ('q', 'quit', 'exit'):
                self.view.bye()
            else:
                typer.echo("Command not recognized")

    @app.command()
    def add(self):
        self.add_contact()

    def add_contact(self):
        first_name = typer.prompt('Enter First Name: ').strip()
        if not first_name.isalpha():
            typer.echo("Error: First Name should only contain letters.")
            return

        last_name = typer.prompt('Enter Last Name: ').strip()
        if not last_name.isalpha():
            typer.echo("Error: Last Name should only contain letters.")
            return

        if self.contact_exists(first_name, last_name):
            typer.echo(f"Error: contact {self.full_name(first_name, last_name)} already exists.")
            return

        number = typer.prompt('Enter Phone Number: ').strip()
        if not number.isdigit() or len(number) != 12:
            typer.echo("Error: invalid phone number.")
            return
        if self.in_dict('Phonenumber', number, self.phonebook.contacts):
            typer.echo(f"The contact {number} is already in the phonebook")
            return

        address = typer.prompt('Enter Address: ').strip()

        contact = Contact(first_name.title(), last_name.title(), number, address)
        self.phonebook.contacts.append(contact)
        self.phonebook.save_data()
        self.view.display_contacts(self.phonebook.contacts)

    def in_dict(self, key, value, dictlist):
        for item in dictlist:
            if getattr(item, key.replace(' ', '_').replace('Phonenumber', 'phone_number').lower()) == value:
                return True
        return False

    def contact_exists(self, first_name, last_name):
        for contact in self.phonebook.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return True
        return False

    def full_name(self, first_name, last_name):
        return " ".join([first_name, last_name])

if __name__ == "__main__":
    app()
