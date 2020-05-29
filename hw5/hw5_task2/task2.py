# Lesson 5 HomeWork - Task 2

"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('my_file.txt', encoding='UTF-8') as user_file:
    content = user_file.read()
    print(f'В файле записаны следующие данные: \n\n{content}')
with open('my_file.txt', encoding='UTF-8') as user_file:
    content = user_file.readlines()
    print(f'\nКоличество строк: {len(content)}')
with open('my_file.txt', encoding='UTF-8') as user_file:
    i = 0
    for line in user_file:
        i += 1
        print(f'В {i}-й строке - {len(line.split())} слов')

user_file.close()
