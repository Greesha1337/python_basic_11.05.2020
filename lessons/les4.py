import sys

from my_lib.my_module import r_sum

print(sys.argv)

_, *vars = sys.argv

tmp = [int(itm) for itm in vars if itm.isdigit()]
print(r_sum([int(itm) for itm in vars if itm.isdigit()]))
# temp = []
# for itm in vars:
#     if itm.isdigit():
#         temp.append(int(itm))


# print(tmp)
#
# print(r_sum([]))


# import time
#
# start = time.time()
# for itm in range(0, 10**3):
#     _ = itm ** 2
# print(time.time() - start)


# from my_lib.my_module import sum as n_sum
#
# print("END IMPORT")
# # print(r_sum([1, 2, 3, 4, 5]))
# print(sum([1, 2, 3, 4, 5]))
# print(n_sum([1, 2, 3, 4, 5]))
#
# if __name__ == "__main__":
#     print(__name__)
#     print(1)


def my_f(n):
    tmp = 0
    while tmp != n:
        yield tmp ** 2
        tmp += 1

for itm in my_f(2):
    print(itm)
