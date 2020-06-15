# Lesson 8 HomeWork - Task 7

"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        print(f'Сумма {self.real, self.imag} и {other.real, other.imag} равна:')
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        print(f'Произведение {self.real, self.imag} и {other.real, other.imag} равно:')
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.imag * other.real + self.real * other.imag)

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)



c_n1 = ComplexNumber(1, 3)
c_n2 = ComplexNumber(4, -5)
c_n3 = ComplexNumber(1, -1)
c_n4 = ComplexNumber(3, 6)

print(c_n1 + c_n2)
print(c_n3 * c_n4)
