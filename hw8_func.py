# Напишіть функцію, що сортує даний словник за ключем.

# - Використовуйте `dict.items()`, щоб отримати список пар кортежів з `d` і відсортувати його за допомогою `sorted()`.
# - Використовуйте `dict()`, щоб перетворити відсортований список назад у словник.
# - Використовуйте параметр `reverse` в `sorted()`, щоб відсортувати словник у зворотному порядку на основі другого аргументу.

# d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
# sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
# sort_dict_by_key(d, True)
# # {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}

def sort_dict_by_key(d, reverse=False):
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=reverse)
    sorted_dict = dict(sorted_items)
    return sorted_dict

d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sorted_dict_asc = sort_dict_by_key(d)
sorted_dict_desc = sort_dict_by_key(d, True)

print(sorted_dict_asc) 
print(sorted_dict_desc) 

# Напишіть функцію sum_by(lst, fn), що обчислює суму списку після зіставлення кожного елемента зі значенням за допомогою наданої функції lambda v : v['n'].

# - Використовуйте `map()` з `fn`, щоб зіставити кожен елемент із значенням за допомогою наданої функції.
# - Використовуйте `sum()`, щоб повернути суму значень.

# sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20

def sum_by(lst, fn):
    return sum(map(fn, lst))

data = [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}]
result = sum_by(data, lambda v: v['n'])
print(result)  


# Напишіть функцію sort_by_indexes(a, b), що сортує один список на основі іншого списку, що містить потрібні індекси.
# - Використовуйте `zip()` і `sorted()`, щоб об’єднати та відсортувати два списки на основі значень `indexes`.
# - Використовуйте list comprehension, щоб отримати перший елемент кожної пари з результату.
# - Використовуйте параметр `reverse` в `sorted()`, щоб відсортувати словник у зворотному порядку на основі третього аргументу.

# a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
# b = [3, 2, 6, 4, 1, 5]
# sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
# sort_by_indexes(a, b, True)
# # ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']

def sort_by_indexes(a, b, reverse=False):
    sorted_pairs = sorted(zip(b, a), reverse=reverse)
    sorted_values = [pair[1] for pair in sorted_pairs]
    return sorted_values

a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]

sorted_result_asc = sort_by_indexes(a, b)
sorted_result_desc = sort_by_indexes(a, b, True)

print(sorted_result_asc)
print(sorted_result_desc)


# Напишіть функцію average, що обчислює середнє значення двох чи більше чисел.
# - Використовуйте `sum()`, щоб підсумувати всі надані `args`
# average(*[1, 2, 3]) # 2.0
# average(1, 2, 3) # 2.0


def average(*args):
    return sum(args) / len(args)

result1 = average(*[1, 2, 3])
result2 = average(1, 2, 3)

print(result1)  
print(result2)  

# Є список словників [{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }]
# Напишіть функцію, що обчислює середнє значення списку після зіставлення кожного елемента зі значенням за допомогою наданої функції lambda x: x['n'].

# - Використовуйте `map()`, щоб зіставити кожен елемент зі значенням, яке повертає `fn`.
# - Використовуйте `sum()`, щоб підсумувати всі зіставлені значення, розділити на `len(lst)`.
# - Пропустіть останній аргумент, `fn`, щоб використовувати функцію ідентифікації за замовчуванням.


def average_dict_list(lst, fn=lambda x: x['n']):
    values = map(fn, lst)
    return sum(values) / len(lst)

data = [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}]
result = average_dict_list(data)

print(result)  


# Напишіть функцію compose(*fns), що виконує композицію функцій справа наліво.

# - Використовуйте `functools.reduce()` для композиції функції справа наліво.
# - Остання (крайня права) функція може приймати один або більше аргументів; решта функцій мають бути унарними.

# add5 = lambda x: x + 5
# multiply = lambda x, y: x * y
# multiply_and_add_5 = compose(add5, multiply)
# multiply_and_add_5(5, 2) # 15

import functools

def compose(*fns):
    return functools.reduce(lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs)), fns)

add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)

result = multiply_and_add_5(5, 2)
print(result)  
