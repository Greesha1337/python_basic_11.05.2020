# Lesson 5 HomeWork - Task 3

"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('salary.txt', encoding='UTF-8') as user_file:
    content = user_file.read()
    print(f'Оклады сотрудников: \n{content}')
with open('salary.txt', encoding='UTF-8') as user_file:
    salary = []
    sad_salary = []
    content = user_file.read().split('\n')
    for line in content:
        surname, line = line.split()
        if int(line) < 20000:
            sad_salary.append(surname)
        salary.append(line)
print(f'У {sad_salary} оклад менее 20000')
print(f'Средний оклад: {sum(map(int, salary)) / len(salary)}')

user_file.close()
