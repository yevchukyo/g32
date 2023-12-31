""""
Якщо відомі три сторони трикутника, але невідома його висота, його площа обчислюється за формулою Герона. Припустімо, задано трикутник зі сторонами a, b і c, 
тоді його площа обчислюється за допомогою таких кроків
Крок 1: Позначте всі розміри даного трикутника.
Крок 2. Обчисліть напівпериметр (s) за формулою s = (a+b+c) / 2
Крок 3: Використовуйте формулу для визначення площі Площа;
A = √[s(s-a)(s-b)(s-c)]
Де, a, b і c — сторони трикутника
Дано трикутник зі сторонами 5 см, 5 см і 6 см. Знайдіть площу і периметр трикутника.
"""
# введення значення сторін трикутника
try:  
    a = float(input("Введіть довжину сторони a: "))
    b = float(input("Введіть довжину сторони b: "))
    c = float(input("Введіть довжину сторони c: "))
    if a > 0 and b > 0 and c>0:
        # Обчислення напівпериметра
        s = (a + b + c) / 2
        # Обчислення площі трикутника за формулою Герона
        area = (s * (s - a) * (s - b) * (s - c))**.5
        # Обчислення периметра трикутника
        perimeter = a + b + c
        # Виведення результатів
        print("Площа трикутника:", area, "см^2")
        print("Периметр трикутника:", perimeter, "см")
    else:
        print("Довжина сторін трикутника повинна бути додатнім числом.")
except ValueError:
    print("Введіть числове значення для довжини сторони.")


#або так,якщо не вводити, а заздалегідь призначити довжини сторін трикутника
import math
# Задані значення сторін трикутника
a = 5
b = 5
c = 6
# Обчислення напівпериметра
s = (a + b + c) / 2
# Обчислення площі трикутника
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# Обчислення периметра трикутника
perimeter = a + b + c
# Виведення результатів
print("Площа трикутника:", area, "см^2")
print("Периметр трикутника:", perimeter, "см")
