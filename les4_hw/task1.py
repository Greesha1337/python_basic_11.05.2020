# Lesson 4 HomeWork - Task 1

"""
Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, emp_hours, emp_rate, emp_prize = argv


print("Имя скрипта: ", script_name)
print("Выработка в часах: ", emp_hours)
print("Ставка в час: ", emp_rate)
print("Премия: ", emp_prize)

salary = int(emp_hours) * int(emp_rate) + int(emp_prize)

print(f"Заработная плата сотрудника составляет: {salary}")


# def salary(emp_hours, emp_rate, emp_prize):
#     result = emp_hours * emp_rate + emp_prize
#     print(f"Заработная плата сотрудника составляет: {result}")
#
#
# emp_hours = float(input("Выработка в часах: "))
# emp_rate = float(input("Ставка в час: "))
# emp_prize = int(input("Премия: "))
#
# salary(emp_hours, emp_rate, emp_prize)
