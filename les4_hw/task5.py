# Lesson 4 HomeWork - Task 5

"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка:
использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""

from itertools import count
from itertools import cycle

while True:
    try:
        start = int(input("Введите целое число начала генератора: "))
        break
    except ValueError:
        print("Это не целое число")

while True:
    try:
        end = int(input("Введите целое число на котором нужно остановиться: "))
        break
    except ValueError:
        print("Это не целое число")


print("Count:")
for el in count(start):
    if el > end:
        break
    else:
        print(el)

user_list = [123, "HELLO", True, None]
c = 0
print("\nCycle:")
for el in cycle(user_list):
    if c > 10:
        break
    print(el)
    c += 1
