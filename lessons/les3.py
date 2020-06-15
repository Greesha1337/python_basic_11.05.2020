#a = 22
def my_pow(a: float) -> float:
    result = a ** 2
    return result


def my_map(func, temp):
    for itm in temp:
        print("START")
        yield func(itm)
        print("YIELD 1 DONE")
        yield func(itm) + 15
        print("YIELD 2 DONE")
        print("CYCLE  DONE")




def my_func(a):
    a += 1

    def help(b):
        return a + b

    return help


# test = my_func(3)
#
# print(test(2))
# print((test(7)))
#
#
# temp = my_map(my_pow, [2, 3, 4, 5])
#
# for itm in temp:
#     print(itm)
#
# print('#' * 20)
# print(list(temp))

def my_except():
    num = 22
    while True:
        try:
            a = int(input("Введите число"))
            result = num / a
            print(type(a), a)
            return result
        except ValueError as error:
            print(error)
            print("ТУТ КОД ОБРАБОТКИ ОШИБКИ")
            continue
        except ZeroDivisionError:
            result = 0
            return result
        finally:
            print("ВЫПОЛНИТСЯ ВСЕГДА")


def my_func2(temp:list) -> float:
    temp.append(2345)
    return sum(temp)


def my_func3(a, b, c, d):
    return sum((a, b, c, d))

a = (1, 2, 3, 4, 5)
print(a)

m_d = {
    "a":2,
    "b":3,
    "c":4,
    "d":5,
}

def my_max(*args, **kwargs):
    print("KWARGS", type(kwargs))
    print(kwargs)
    print("ARGS", type(args))
    result = float("inf") * -1
    for itm in args:
        if result < itm:
            result = itm
    return result


m_l = [2, 3, 4, 5]
#result = my_func3(**m_d)
#result = my_func3(*m_l[:4])
result = my_max(1, 2, 3, 4, 5, 22, 66, 1, 3, 77, 87, 222, 33, key=my_pow)

print(result)

# a, b, c, *d = input("HELLO").split(" ")
# print(a, b, c, d)

# def print(*args, **kwargs):
#     pass

#print(*m_l, end="-----")

#result = my_func3(b=2, c=3, a=6, d=17)
#print(a)



# print(a)
# result = my_func2(a)
# print(a)
# print(result)

#result = my_except()

# print("ТУТ КОД ПРОГРАММЫ ДАЛЬШЕ")
# print(result)

#lambda x: x ** 2
