# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    n = input('Введите целое число\n')
    if n.isdigit():
        n = abs(int(n))
        break
    else:
        print('Вы ввели неверное число, повторите')

maximum_number = 0
while n > 0:
    if (n % 10) > maximum_number:
        maximum_number = n % 10
    n = n // 10
print('Максимальное число: ', maximum_number)
