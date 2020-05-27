# Lesson 5 HomeWork - Task 5

"""
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

while True:
    try:
        with open('numbers.txt', 'w+') as file:
            numbers = input('Введите числа через пробел для записи в файл: ')
            file.writelines(numbers)
            user_number = numbers.split()
            print(f'Сумма чисел в файле: {sum(map(float, user_number))}')
            break
    except ValueError:
        print('Неправильный ввод')
    except IOError:
        print('Ошибка ввода-вывода')

file.close()
