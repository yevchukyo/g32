#Напишіть програму розпаковки кортежу на кілька змінних.

#створення кортежу
tuple1 = (1, 2, 3)
a, b, c = tuple1
#виведення значення змінних
print("a = ",a)  
print("b = ", b)  
print("c = ", c) 


#якщо нам потрібні не всі змінні з кортежу, а конкретні, то можна зробити наступним чином:
#створення кортежу
tuple2 = (4, 5, 6, 7)
d, _, _, e = tuple2
#виведення значення змінних
print("d = ", d)  
print("e = ", e)
