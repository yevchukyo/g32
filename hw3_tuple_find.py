#Напишіть програму Python, щоб перевірити, чи існує елемент у кортежі.
#створення кортежу
tuple1 = ('apple', 'banana', 'cherry','cucumber')
#введення елементу для перевірки
element = input("Введіть елемент: ")
#виведення результатів
if element in tuple1:
    print("Елемент", element, "знаходиться у кортежі.")
else:
    print("Елемент", element, "не знаходиться у кортежі.")