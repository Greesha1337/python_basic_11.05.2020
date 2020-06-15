# Lesson 8 HomeWork - Task 4, 5, 6

"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
"""


class Warehouse:

    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        state = f'На складе {self.name}:\n'
        if self.items:
            for i, item in enumerate(self.items):
                state += f'{i+1}: {item}\n'
        else:
            state += 'Склад пустой\n'
        return state

    def add_item(self, equipment):
        self.items.append(equipment)

    def remove_item(self, equipment):
        if equipment not in self.items:
            raise KeyError(equipment)
        self.items.remove(equipment)

    def move(self, equipment, another_warehouse):
        self.remove_item(equipment)
        another_warehouse.add_item(equipment)


class Equipment:
    def __init__(self, name, model, price, count):
        if (type(price) is not (int or float)) or price < 0:
            raise ValueError('Цена должна быть положительным числом')
        if (type(count) is not (int or float)) or count < 0:
            raise ValueError('Количество должно быть положительныии числом')

        self.name = name
        self.model = model
        self.price = price
        self.count = count

    def __str__(self):
        return f'{self.name} {self.model} по цене {self.price} руб, в количестве - {self.count} шт.'


class Printer(Equipment):
    name = 'Принтер'


class Scanner(Equipment):
    name = 'Сканер'


class Xerox(Equipment):
    name = 'Ксерокс'


eq_1 = Printer('Kyocera', 'P6230cdn', 28499, 5)
eq_2 = Scanner('Canon', 'DR-F120', 24599, 3)
eq_3 = Xerox('Xerox', 'B1025DNA', 67299, 10)

wh_main = Warehouse('Главный')
wh_spb = Warehouse('Санкт-Петербург')
wh_msk = Warehouse('Москва')

wh_main.add_item(eq_1)
wh_main.add_item(eq_2)
wh_main.add_item(eq_3)

print(wh_main)

wh_main.move(eq_3, wh_spb)
print(wh_main)
print(wh_spb)

wh_main.move(eq_2, wh_msk)
print(wh_main)
print(wh_msk)

wh_main.move(eq_1, wh_spb)
print(wh_main)
print(wh_spb)
print(wh_msk)

try:
    wh_main.move(eq_1, wh_spb)
except KeyError as e:
    print('На складе нет оборудования')


try:
    eq_4 = Printer('HP', '107r', -6999, 2)
    print(eq_4)
except ValueError as e:
    print(e)
