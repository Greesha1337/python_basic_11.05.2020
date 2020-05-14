# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

while True:
    n = input('Введите целое число n\n')
    if n.isdigit():
        n_2 = (n + n)
        n_3 = (n + n + n)

        summ = int(n) + int(n_2) + int(n_3)
        print('n+nn+nnn = ', summ)
        break
    else:
        print('Вы ввели неверное число, повторите')
