#Напишіть програму для перевірки, чи є введене число простим
#Просте число - це натуральне число більше 1, яке має лише два дільники: 1 і саме число

number = input("Введіть число: ")
try:
    number = int(number)
# Перевірка числа на простоту
    if number < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
# Виведення результату
    if is_prime:
        print(number, "є простим числом")
    else:
        print(number, "не є простим числом")
except ValueError:
    print("Введене значення не є цілим числом.")