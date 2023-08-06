#1. за допомогою list comprehension створити список квадратів всіх чисел у діапазоні від 1 до 9: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x**2 for x in range(10)]
print(squares)

#2. за допомогою list comprehension створити список, де всі цифри діляться на 5 без остатку, в диапазоні від 0 до 100: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

div_5 = [x for x in range(100) if x % 5 == 0]
print(div_5)

#3. за допомогою list comprehension створити список, де всі цифри діляться на 3 і 6 без остатку, в диапазоні від 0 до 50: [3, 9, 15, 21, 27, 33, 39, 45]

div_3_6 = [x for x in range(50) if x % 3 == 0 and x % 6 == 0]
print(div_3_6)

#3. за допомогою list comprehension створити список, де всі цифри діляться на 3 і 6 без остатку, в диапазоні від 0 до 50: [3, 9, 15, 21, 27, 33, 39, 45]
#цей код виведе саме такий результат як в умові

div6_3 = [x + 3 for x in range(50) if (x % 6) == 0 and (x + 3) < 50]
print(div6_3)

#4. за допомогою list comprehension створити список, що містить перші літери кожного слова  речення 'The rocket came back from Mars'
sentence = 'The rocket came back from Mars'
first_letters = [word[0] for word in sentence.split()]
print(first_letters)

#5. за допомогою list comprehension замінити в "all, max, matrix, awesome, appalling, abba" літеру a у кожному слові на #.

words = "all, max, matrix, awesome, appalling, abba"
modified_words = [word.replace('a', '#') for word in words.split(', ')]
print(modified_words)

#6.  переписавши код за допомогою list comprehension:
# even_numbers = [] 
# for x in range(10):
#     if x % 2 == 0:
#         even_numbers.append(x)
# print(even_numbers) # [0, 2, 4, 6, 8]

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

#7.  Є список numbers = [121, 544, 111, 99, 77]  
# Вибрати тільки ті числа, що діляться на 11
# [121, 99, 77]

numbers = [121, 544, 111, 99, 77]
div_11 = [num for num in numbers if num % 11 == 0]
print(div_11) 

#8.створити list comprehension, що містить парні числа від 2 до 9998 включно

even_numbers = [num for num in range(2, 9999) if num % 2 == 0]
print(even_numbers)

# 9. Написати фільтр, який відбирає літери у реченні, що не є голосні 
# sentence = 'the rocket came back from mars'
# # ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']

sentence = 'the rocket came back from mars'
vowels = 'aeiouy'
filtered_letters = [letter for letter in sentence if letter.lower() in vowels]
print(filtered_letters)

#10. знайти квадрат лише парних чисел у діапазоні range(10)
# [0, 4, 16, 36, 64]

y = [x**2 for x in range(10) if x % 2 == 0]
print(y)

#11. Зформувати таблицю множення чисел від 1 до 5. 
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]

table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
print(table)

#12 Є 2 кортежі a = (1, 3, 5) і b = (2, 4, 6)
# Згенерувати всі пари з a і b
# [(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4), (5, 6)]

a = (1, 3, 5)
b = (2, 4, 6)
pairs = [(x, y) for x in a for y in b]
print(pairs)

# 13 Є 2 кортежі a = (1, 3, 5) і b = (2, 4, 6)
# Згенеруйте всі пари з a і b, за умови  a > b
# [(3, 2), (5, 2), (5, 4)]

a = (1, 3, 5)
b = (2, 4, 6)
pairs = [(x, y) for x in a for y in b if x > y]
print(pairs)

# 14. Є матриця  matrix = [[1, 2], [3,4], [5,6], [7,8]]
# Транспонувати матрицю за допомогою List Comprehension
# [[1, 3, 5, 7], [2, 4, 6, 8]]

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
tmatrix = [list(row) for row in zip(*matrix)]
print(tmatrix)

