# Lesson 8 HomeWork - Task 2

"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDiv:
    def __init__(self, *args):
        self.args = args

    @staticmethod
    def divide():
        while True:
            try:
                denominator = float(input('Введите делимое: '))
                break
            except ValueError:
                print(f'Неправильный ввод')

        while True:
            try:
                divider = float(input('Введите делитель: '))
                if divider == 0:
                    return f'На ноль делить нельзя'
                else:
                    return denominator / divider
            except ValueError:
                print(f'Неправильный ввод')


div = ZeroDiv
print(ZeroDiv.divide())
