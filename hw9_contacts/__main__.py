"""hw9_contacts/__main__.py"""

from hw9_contacts import cli
from hw9_contacts import __app_name__

def main():
    print(F"This is my file: {__file__} to test Python's execution methods.")
    print(F"The variable __name__ tells me which context this file is running in.")
    print("The value of __name__ is:", repr(__name__))
    
    cli.app(__app_name__)  # Додайте цей рядок, якщо хочете викликати вашу командну оболонку
    
if __name__ == '__main__':
    main()


