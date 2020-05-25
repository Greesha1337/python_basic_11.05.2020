# Lesson 3 HomeWork - Task 1

"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def degree_func(a, b):
    """Возвращает частное от деления

    a, b - позиционные аргументы, запрашиваемые у пользователя
    """

    while True:
        try:
            return a / b
        except ZeroDivisionError:
            return 'На ноль делить нельзя!'


while True:
    try:
        a = int(input('Введите первое число: '))
        break
    except ValueError:
        print('Неверный ввод')

while True:
    try:
        b = int(input('Введите второе число: '))
        break
    except ValueError:
        print('Неверный ввод')

print(f'Результат деления первого числа на второе: {degree_func(a, b)}')
print(f'Результат деления второго числа на первое: {degree_func(b, a)}')

# Первая попытка
# while True:
#     try:
#         a = int(input('Введите делимое: '))
#         b = int(input('Введите делитель: '))
#         result = a / b
#     except ValueError:
#         print('Неверный ввод')
#         continue
#     except ZeroDivisionError:
#         return 'На ноль делить нельзя!'
#
#     return result

# Вторая попытка
# while True:
#     try:
#         a = int(input('Введите делимое: '))
#         break
#     except ValueError:
#         print('Неверный ввод')
#
# while True:
#     try:
#         b = int(input('Введите делитель: '))
#         result = a / b
#     except ValueError:
#         print('Неверный ввод')
#         continue
#     except ZeroDivisionError:
#         return 'На ноль делить нельзя!'
#
#     return result
