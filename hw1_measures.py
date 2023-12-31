"""
Найпростіший спосіб перетворити будь-яке вказане значення кілометрів у милі в Python — це визначити коефіцієнт перетворення.
Коефіцієнт перетворення — це змінна, у якій ми зберігаємо число, яке потрібно помножити на задане значення кілометрів, щоб отримати результат у милях.
Написати програму Python для перетворення кілометрів у милі за формулою: 
1 км = 0,621371 милі

Написати програму Python для перетворення градусів Цельсія у Фаренгейт за формулою:
T(℉) = T(℃) x 9/5 + 32
"""

# Перетворення кілометрів у милі
try:
    kilometers = float(input("Введіть значення в кілометрах: "))
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    print(f"{kilometers} км = {miles} миль")
except ValueError:
    print("Введіть числове значення для кілометрів.")

# Перетворення градусів Цельсія у Фаренгейт
try:
    celsius = float(input("Введіть значення в градусах Цельсія: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius} C = {fahrenheit} F")
except ValueError:
    print("Введіть числове значення для градусів Цельсія.")