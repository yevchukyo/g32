"""У вас є файл із такими реченнями (Piper.txt): 
Peter Piper picked a peck of pickled peppers. 
A peck of pickled peppers Peter Piper picked. 
Where's the peck of pickled peppers Peter Piper picked.

Потрібно вставити нове речення (If Peter Piper picked a peck of pickled peppers) після другого речення  в той самий рядок. 
Бажаний результат: 
Peter Piper picked a peck of pickled peppers. 
A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers. 
Where's the peck of pickled peppers Peter Piper picked.
Тому найкраща практика:
-	Прочитати речення з файлу,
-	Внести необхідні зміни,
-	Записати його в новий файл. 
Використовуйте метод splitlines(), який повертає список рядків, розбитих на межі рядків.
"""

def insert_sentence(input_file, output_file, new_sentence):
    with open(input_file, 'r') as file:
        lines = file.read().splitlines()

    # розділяємо рядок із трьох речень на окремі речення
    sentences = lines[0].split('. ')

    # додаємо наше нове речення до другого речення, та додаємо роздільний знак
    sentences[1] += '. ' + new_sentence

    # обєднуємо  речення знову в один рядок із додаванням роздільних знаків
    lines[0] = '. '.join(sentences)

    with open(output_file, 'w') as file:
        file.write('\n'.join(lines))

# шлях до вхідного файлу
input_file_path = 'hw6_input.txt'

# шлях до вихідного файлу
output_file_path = 'hw6_output.txt'

# речення для вставки
new_sentence = "If Peter Piper picked a peck of pickled peppers"

insert_sentence(input_file_path, output_file_path, new_sentence)

#виводимо результат
print("Змінений файл (hw6_output.txt):")
with open(output_file_path, 'r') as file:
    print(file.read())

print("\nПочатковий файл (hw6_input.txt):")
with open(input_file_path, 'r') as file:
    print(file.read())
