"""
Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел.

У пользователя необходимо запрашивать новый элемент рейтинга.

Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
print(my_list)

new_element = input("Введите новый элемент рейтинга\n")
new_element = int(new_element)

for el in range(len(my_list)):
    if my_list[el] == new_element:
        my_list.insert(el+1, new_element)
        break
    elif my_list[0] < new_element:
        my_list.insert(0, new_element)
        break
    elif my_list[-1] > new_element:
        my_list.append(new_element)
        break
    elif my_list[el] > new_element > my_list[el + 1]:
        my_list.insert(el + 1, new_element)
        break
print(my_list)
