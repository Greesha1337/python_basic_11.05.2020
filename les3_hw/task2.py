# Lesson 3 HomeWork - Task 2

"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
    имя,
    фамилия,
    год рождения,
    город проживания,
    email,
    телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
print("Введите ваши данные\n")


def user_data(name, surname, b_year, city, mail, phone_number):
    """Реализует вывод данных одной строкой."""
    return " ".join([name, surname, b_year, city, mail, phone_number])


name = input("Имя: ")
surname = input("Фамилия: ")
b_year = input("Год рождения: ")
city = input("Город проживания: ")
mail = input("e-mail: ")
phone_number = input("Номер телефона: ")

print(user_data(name, surname, b_year, city, mail, phone_number))
