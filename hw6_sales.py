"""Є файл sales.txt, який містить щомісячні дані про продажі товарів. 
Знайти у файлі рядок про продаж певного товару, надрукувати цей рядок та його номер. 
Відкрити файл у режимі читання. 
Використовуйте метод readlines(), щоб отримати всі рядки з файлу у формі об’єкта списку.
Використовуйте цикл для повторення кожного рядка з файлу.
В кожній ітерації циклу використовуйте умову if, щоб перевірити, чи присутній рядок у поточному рядку, і, якщо присутній, виведіть поточний рядок разом із номером рядка."""


# додам ще перевірку на введення корекної назви файлу та перевірку на наявність товару в списку

def find_product_sale(filename, product_name):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines, 1):
                if product_name in line:
                    print(f"Знайдено рядок у файлі {filename}, рядок номер {line_number}: {line.strip()}")
        if not any(product_name in line for line in lines):
            print(f"Товар з назвою '{product_name}' не знайдено у файлі '{filename}'")
    except FileNotFoundError:
        print(f"Файл з назвою '{filename}' не існує")

def main():
    filename = input("Введіть назву файлу: ")
    product_name = input("Введіть назву продукту (Product N): ")
    find_product_sale(filename, product_name)

if __name__ == "__main__":
    main()