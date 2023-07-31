"""Модуль pathlib має функцію read_text(), що читає текстовий файл 
path.read_text().count("\n") читає текстовий файл і обчислює кількість рядків шляхом підрахунку рядків.
len(path.read_text().split()) читає текстовий файл і обчислює кількість слів
len(path.read_text()) читає текстовий файл і обчислює кількість символів, знаходячи довжину рядка.

Написати скрипт, що може читати один або декілька текстових файлів і повідомляти, скільки рядків, слів і символів містить кожен із файлів. """


from pathlib import Path

def count_lines_words_chars(file_path):
    try:
        # створюємо обєкт Path для файлу
        path = Path(file_path)

        # читаємо вміст файлу
        content = path.read_text()

        # обчислюємо кількість рядків
        num_lines = content.count("\n")

        # обчислюємо кількість слів
        num_words = len(content.split())

        # обчислюємо кількість символів
        num_chars = len(content)

        # результати
        return num_lines, num_words, num_chars
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено. Переконайтесь, що він існує.")

def main():
    # вводимо шлях до файлу або файлів (наприклад, з попередніх завданнь d:\projects\hw6_sales.txt d:\projects\hw6_output.txt d:\projects\hw6_input.txt)
    file_paths = input("Введіть шлях до файлу або файлів: ").split()

    for file_path in file_paths:
        num_lines, num_words, num_chars = count_lines_words_chars(file_path)

        print(f"\nІнформація про файл '{file_path}':")
        print(f"Кількість рядків: {num_lines}")
        print(f"Кількість слів: {num_words}")
        print(f"Кількість символів: {num_chars}")

if __name__ == "__main__":
    main()
