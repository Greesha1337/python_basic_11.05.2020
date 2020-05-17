"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

season_list = ["Зима", "Весна", "Лето", "Осень"]
season_dict = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}


while True:
    month = input("Введите номер месяца\n")
    if month.isdigit():
        month = int(month)
        if 1 <= month <= 12:
            if 1 <= month <= 2 or month == 12:
                print(season_dict.get(1))
                print((season_list[0]))
            elif 3 <= month <= 5:
                print(season_dict.get(2))
                print((season_list[1]))
            elif 6 <= month <= 8:
                print(season_dict.get(3))
                print((season_list[2]))
            elif 9 <= month <= 11:
                print(season_dict.get(4))
                print((season_list[3]))
            break
        else:
            print("Неверный номер месяца")
    else:
        print("Неверный номер месяца")
