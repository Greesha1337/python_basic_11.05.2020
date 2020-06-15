# Lesson 7 HomeWork - Task 2

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @property
    @abstractmethod
    def square(self) -> float:
        pass

    @property
    @abstractmethod
    def params(self) -> float:
        pass

    @property
    @abstractmethod
    def str(self) -> str:
        pass


class Coat(Clothes):

    def __init__(self, name: str, size: float):
        self.name = name
        self.__size = size

    @property
    def square(self) -> float:
        return self.__size / 6.5 + 0.5

    @property
    def params(self) -> float:
        return self.__size

    @property
    def str(self):
        return 'Расход ткани на {} - {:.2f} м2'.format(self.name, self.square)


class Suit(Clothes):

    def __init__(self, name: str, height: float):
        self.name = name
        self.__height = height

    @property
    def square(self) -> float:
        return 2 * self.__height + 0.3

    @property
    def params(self) -> float:
        return self.__height

    @property
    def str(self):
        return 'Расход ткани на {} - {:.2f} м2'.format(self.name, self.square)


coat = Coat('Честерфилд', 7)
suit = Suit('Смокинг', 4)
print(coat.str)
print(suit.str)
print('Всего израсходовано ткани - {:.2f} м2'.format(coat.square + suit.square))
