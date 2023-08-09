"""hw9_contacts/models.py"""

import pickle
import os.path
from hw9_contacts import DATABASE



def read_file() -> list[dict]:
    data = []
    if os.path.isfile(DATABASE):
        with open(DATABASE, 'rb') as f:
            data = pickle.load(f)
    return data

def get_contacts() -> list[dict]:
    data = read_file()
    if data is None:
        data = []
    return data

def save_contacts(records: list[dict]) -> None:
    if os.path.isfile(DATABASE):
        with open(DATABASE, 'wb') as f:
            pickle.dump(records, f)

def clear_contacts():
    save_contacts([])  # Зберігаємо пустий список контактів
    
def main():
    print(F"This is my file: {__file__} to test Python's execution methods.")
    
    print("The value of __name__ is:", repr(__name__))
    
if __name__ == '__main__':
    main()