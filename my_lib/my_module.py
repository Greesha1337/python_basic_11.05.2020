def sum(items):
    print('summ = ')
    result = 0
    for itm in items:
        result += itm
    return result


def r_sum(items):
    return items[0] + r_sum(items[1:]) if items else 0

print("HELLO")
print(__name__)