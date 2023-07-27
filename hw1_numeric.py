""""
Напишіть програму, що приймає ціле <число> та друкує текст  
The next number for the number <число> is <число>+1. The previous number for the number <число> is <число>-1. 
"""

number = input("Введіть число: ")

if number.isdigit():
    number = int(number)
    next_number = number + 1
    previous_number = number - 1

    print("The next number for the number", number, "is", next_number)
    print("The previous number for the number", number, "is", previous_number)
else:
    print("Введене значення не є цілим числом.")