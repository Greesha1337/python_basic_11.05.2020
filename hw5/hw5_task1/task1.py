# Lesson 5 HomeWork - Task 1

"""
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('user_file.txt', 'a', encoding='UTF-8') as file:

    while True:
        user_words = input('Введите данные для записи в файл: ')
        if user_words == '':
            break
        file.write(user_words + '\n')

file.close()
