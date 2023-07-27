"""Використовуючи словник, видалити всі дублі слів з даного речення: 
Python is great and Java is also great
Потрібно отримати: Python is great and Java also"""

#перший варіант рішення. я вирішив розкидати речення на 2 словника та обєднати унікальні елементи кожного словника в один.
#не дуже раціональне рішення, щодо мене. але працює))))
sentence = "Python is great and Java is also great"
# розділяємо речення на  слова
words = sentence.split()
# створюємо два словника для відстеження унікальних слів
word_dict1 = {}
word_dict2 = {}
# розкидуємо слова на два словника
for word in words:
    if word not in word_dict1:
        word_dict1[word] = 1
    else:
        word_dict2[word] = 1
# поєдную два словника за допомогою оператора |
merged_dict = word_dict1 | word_dict2
# створюю нове речення, додаючи унікальні слова зі словника
new_sentence = " ".join(merged_dict.keys())
print(new_sentence)

#інший варіант рішення. більш прогресивне
sentence = "Python is great and Java is also great"
# розділяємо речення на  слова
words = sentence.split()
# створюю словник для відстеження кількості окремого слова
word_count = {}
# формую нове речення, включаючи тільки перше входження слова
new_sentence = []
for word in words:
    if word not in word_count:
        new_sentence.append(word)
        word_count[word] = 1
new_sentence = " ".join(new_sentence)
print(new_sentence)