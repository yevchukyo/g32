# model.py
import configparser

class Contact:
    def __init__(self, first_name, last_name, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

class Phonebook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = []
        self.load_data()

    def load_data(self):
        config = configparser.ConfigParser()
        config.read(self.file_path)
        
        for section in config.sections():
            contact = Contact(
                config.get(section, 'First name'),
                config.get(section, 'Last name'),
                config.get(section, 'Phonenumber'),
                config.get(section, 'Address')
            )
            self.contacts.append(contact)

    def save_data(self):
        config = configparser.ConfigParser()
        for i, contact in enumerate(self.contacts):
            section_name = f'Contact_{i}'
            config[section_name] = {
                'First name': contact.first_name,
                'Last name': contact.last_name,
                'Phonenumber': contact.phone_number,
                'Address': contact.address
            }
        with open(self.file_path, 'w') as configfile:
            config.write(configfile)
