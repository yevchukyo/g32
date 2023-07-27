
"""Створити просту гру на відгадування чисел, яка дозволяє користувачеві вгадувати випадкове число від 1 до 100.  
Програма повинна надавати підказки користувачеві після кожного вгадування, вказуючи, чи було його припущення завеликим або замалим,  доки користувач вгадує правильне число.
Почніть з імпорту модуля random, який дозволить вам згенерувати випадкове число. 
Згенеруйте випадкове число від 1 до 100 за допомогою функції randint() із модуля random і призначте його змінній.
Створіть цикл, де користувачі вгадуватиме число, поки не вгадає правильно. У циклі запропонуйте користувачеві ввести число за допомогою функції input().
Додайте умовний оператор у середині циклу, який перевіряє, чи припущення користувача є правильним, занадто високим чи малим. 
Якщо припущення вірне, роздрукуйте вітальне повідомлення та вийдіть із циклу. Якщо припущення завелике або занизьке, 
надрукуйте повідомлення-підказку, щоб допомогти користувачеві правильно вгадати число. 
"""

import random
# генеруємо випадкове число від 1 до 100
secret_number = random.randint(1, 100)

#додаємо підрахунок кількості спроб вгадати число
attempts = 0

# Цикл на вгадування з підказкою
while True:
    #вводимо число - відповідь, виключаємо введення інших символів
    try:
        number = int(input("Введіть свою відповідь: "))
    except ValueError:
        print("Введіть ціле число.")
        continue
    # збільшуємо кількість спроб на 1
    attempts += 1
    #перевіряємо чи відгадав користувач
    if number == secret_number:
        print("Бінго! Ви вгадали число за", attempts, "спроб.")
        break
    elif number < secret_number:
        print("Мало. Спробуйте ще раз.")
    else:
        print("Багато. Спробуйте ще раз.")
#при такій реалізації в кількість спроб буде враховуватися тільки введені числа. тобто якщо користувач буде вводити літері чи інші символи або порожнє значення,
#то воно не буде зараховуватися в лічильник спроб. 