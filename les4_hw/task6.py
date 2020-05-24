# Lesson 4 HomeWork - Task 6

"""
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка:
факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from itertools import count
from math import factorial


def fact():
    for n in count(1):
        yield factorial(n)


while True:
    while True:
        try:
            n = int(input("Введите целое положительное число: "))
            break
        except ValueError:
            print("Неправильный ввод")
    if n < 0:
        print("Неправильный ввод")
    else:
        break

x = 0
for el in fact():
    if x < n:
        print(f"Факториал {x + 1} равен: {el}")
        x += 1
    else:
        break
