



# Імпортуємо функцію tabulate з модуля tabulate для красивого виведення таблиць.
from tabulate import tabulate

# Задаємо заголовок програми.
TITLE = 'Your Dict Phonebook'

# Функція, яка об'єднує ім'я та прізвище у повне ім'я.
def full_name(first_name, last_name):
    return " ".join([first_name, last_name])

# Функція, яка виводить привітання з заголовком і запитує користувача, що він хоче зробити.
def hello():
    print(f"Hi! It's me, {TITLE}")
    return input("What You wanna do? [a(dd)|l(ist)|f(ind)|r(emove)|c(lear)|q(uit))]: ")

# Функція, яка виводить прощання.
def bye():
    print(f"Thank You for using {TITLE}")
    exit(0)

# Вхідні дані у вигляді словника, який містить декілька контактів.
data = {
    '0': {'First name': 'Mary', 'Last name': 'Ann', 'Phonenumber': '123456700000', 'Address': 'Some City, 1, Some Str.'},
    '1': {'First name': 'John', 'Last name': 'Doe', 'Phonenumber': '111111100000', 'Address': 'Some City1, 2, Some Str1.'},
    '2': {'First name': 'John', 'Last name': 'Dick', 'Phonenumber': '222222200000', 'Address': 'Some City2, 3, Some Str2.'},
}

# Створюємо порожній список контактів, де кожен контакт буде представлений словником.
contacts = []

# Проходимо по елементах словника data та перетворюємо кожен контакт у словник, додавши йому ідентифікатор.
for id in data:
    contact = {}
    for key in data[id]:
        contact['id'] = id
        contact[key] = data[id][key]
    contacts.append(contact)

# Функція, яка виводить список контактів у вигляді таблиці.
def contact_list(contacts):
    print(tabulate(contacts, headers='keys', tablefmt="fancy_grid"))

# Функція, яка перевіряє, чи існує задане значення ключа у списку словників.
def in_dict(key, value, dictlist):
    for item in dictlist:
        if item[key].lower() == value:
            return True
    return False

# Функція для додавання нового контакту.
def add_contact():
    contact = {}
    
    number = input('Enter Phone Number: ').strip()
    #перевірка номеру на довжину, правильність введення, унікальність
    if not number.isdigit() or len(number) != 12:
        print("Error: invalid phone number.")
        return None
    if in_dict('Phonenumber', number, contacts):
            print(f"The contact {number} is already in the phonebook")
            return
    contact['Phonenumber'] = number

    first_name = input('Enter First Name: ').strip()
    last_name = input('Enter Last Name: ').strip()
    
    #перевірка вимоги унікальності значення повного імені  
    if in_dict('First name', first_name, contacts) and in_dict('Last name', last_name, contacts):
        print(f"Error: contact {full_name(first_name, last_name)} already exists.")
        return None
    contact['First name'] = first_name.title()
    contact['Last name'] = last_name.title()
#ми використовуємо title() для коректного форматування імен і прізвищ у рядках, 
#які використовуються в словнику контактів, щоб вони виглядали зрозуміло та читабельно для користувача.

    address = input('Enter Address: ').strip()
    contact['Address'] = address

    return {
            'First name': first_name.title(),
            'Last name': last_name.title(),
            'Phonenumber': number,
            'Address': address
            }
        
#функція перевіряє наявність заданого елемента el у списку lst. результат зберігається у змінній result.
def lookup_element(lst, el):
    result = []

#виводить контакти зі списку "result" у вигляді таблиці за допомогою бібліотеки tabulate.      
def show_contact(result):
    columns = ['First Name', 'Last Name', 'Number', 'Address']
    print(tabulate(result, headers=columns, tablefmt="fancy_grid"))


#aункція пошуку контакта в книзі по будь-якому полю. тобто перевіряє наявність контактів зі значенням target у словнику contacts.
#hезультат зберігається у списку founded_contacts.
def lookup_contact(target):
    founded_contacts = []
    for key in list(contacts[0].keys())[0:4]:
        for index, contact in enumerate(contacts):
            if contact[key] == target:
                founded_contacts.append(contact)
    return founded_contacts

#функція видалення певного контакту    
def remove_contact(index):
    if index in range(len(contacts)):
        confirm = input("Are You sure You wish to delete this contact? (y|n): ")
        if confirm.lower() in ('yes', 'y'):
            contacts.pop(index)
        else:
            return
    else:
        print(f"Error: element with index {index} does not exist")
#функція очищення телефонної книги. після очищення виводить результат - у вигляді таблиці із заголовками.
def clear_phonebook():
    contacts.clear()
    print("Phonebook cleared")
    columns = ['First Name', 'Last Name', 'Number', 'Address']
    print(tabulate(contacts, headers=columns, tablefmt="fancy_grid"))
# Головне тіло програми. Доречі, можна перетворити на цикл. щоб програма працювала по колу, а не перезапускати.
#     

# Головний цикл програми
while True:
    command = hello()
    if command in ('a', 'add'):
        contact = add_contact()
        if contact:
            contact['id'] = str(len(contacts))
            contacts.append(contact)
            contact_list(contacts)
    elif command in ('f', 'find'):
        el = input("What You're looking for? :").strip().title()
        if lookup_contact(el):
            contact_list(lookup_contact(el))
        else:
            print(f"Sorry, nothing found for {el}")
    elif command in ('l', 'list'):
        contact_list(contacts)
        order = input("Enter order by name = 1 or order by surname = 2: ")
        while not order.isdigit():
            print("Invalid input. Please enter a valid option.")
            order = input("Enter order by name = 1 or order by surname = 2: ")

        order = int(order)
        match order:
            case 1:
                sortedbook = sorted(contacts, key=lambda x: x['First name'])
                contact_list(sortedbook)
            case 2:
                sortedbook = sorted(contacts, key=lambda x: x['Last name'])
                contact_list(sortedbook)
            case _:
                print ('Contact list not sorted')
                contact_list(contacts)
  
    elif command in ('r', 'remove', 'delete'):
        index = int(input("What contact You wanna remove? :"))
        remove_contact(index)
        contact_list(contacts)

    elif command in ('c', 'clear'):
        clear_phonebook()
  
    elif command in ('q', 'quit', 'exit'):
        bye()

    else:
        print("Command not recognized")
