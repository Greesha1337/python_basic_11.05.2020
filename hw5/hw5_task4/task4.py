# Lesson 5 HomeWork - Task 4

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus = {'One': 'Один',
       'Two': 'Два',
       'Three': 'Три',
       'Four': 'Четыре',
       }
new_list = []
with open('user_file.txt', encoding='UTF-8') as translator:
    for n in translator:
        n = n.split(' ', 1)
        new_list.append(rus[n[0]] + ' ' + n[1])
    print(new_list)

with open('user_file_translated.txt', 'w', encoding='UTF-8') as translated:
    translated.writelines(new_list)

translated.close()
translator.close()
