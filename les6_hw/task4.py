# Lesson 6 HomeWork - Task 4

"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def show_speed(self):
        return f'{self.speed} км/ч'

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина'
        else:
            return f'{self.name} - не полицейская машина'


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины {self.name} - {self.speed} км/ч')

        if self.speed > 60:
            return f'Превышение скорости на {int(self.speed) - 60} км/ч'


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} - {self.speed} км/ч')

        if self.speed > 40:
            return f'Превышение скорости на {int(self.speed) - 40} км/ч'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


priora = TownCar('Priora', 'Black', 70, False)
solaris = WorkCar('Solaris', 'Yellow', 90, False)
mondeo = PoliceCar('Mondeo', 'White', 120, True)
bmw = SportCar('Bmw', 'Red', 220, False)

print(priora.turn_right())
print(f'Если {solaris.turn_left()}, тогда {bmw.stop()}')
print(f'{mondeo.go()}, со скоростью - {mondeo.show_speed()}')
print(f'Цвет {solaris.name} - {solaris.color}')
print(f'{solaris.show_speed()}')
print(f'{mondeo.police()}')
print(f'{bmw.police()}')
print(mondeo.stop())
print(f'{priora.show_speed()}')
