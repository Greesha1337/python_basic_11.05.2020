# Lesson 3 HomeWork - Task 3

"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """Возвращает сумму двух максимальных чисел."""
    if a >= c and b >= c:
        return a + b
    elif a <= b <= c:
        return b + c
    else:
        return a + c


a, b, c = map(int, input('Введите три числа\n').split())
print(f'Результат: {my_func(a, b, c)}')
