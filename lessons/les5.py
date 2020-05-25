# import json

#file = open("input.txt", "r", encoding="UTF-8")

# for line in file:
#     print(line, end="")

# print(file.read())

#print(file.readlines())

#print(file.readline())

# print(file.read(8))
# print(file.read(8))


# file = open('input.txt', 'r', encoding='UTF-8')
# try:
#     print(file.read())
# except IOError:
#     print('Ошибка')
# finally:
#     file.close()

# with  open('output1.txt', 'wb') as out_file:
#     content = bytes('HELLO MY DEAR FRIENDS, Это байтовая строка', encoding='UTF-8')
#     print(content)
#     out_file.write(content)

# data = {
#     'key1': [1, 2, 3],
#     'key2': True,
#     'key3': None,
#     'key4': 'HELLO МИР"',
#     'key5': (1, 2, 3, 4),
# }
#
# new_data = [data, data]
#
# j_data = json.dumps(new_data, ensure_ascii=False)
#
# print(j_data)
#
# with open('j_data.json', 'r') as j_file:
#     print(json.load(j_file))

import os

# print(os.listdir('.'))
# print(os.path.isdir('lessons'))
dir_path_root = os.path.dirname(__file__)
# print(os.path.dirname(__file__))
# print(__file__)

file_name = 'output1.txt'

full_path = os.path.join(dir_path_root, file_name)
#print(full_path)

#os.rename(full_path, 'new_name.txt')

# with open(full_path, 'r') as in_file, open('new_copy.txt', 'w') as cop_file:
#     cop_file.write(in_file.read())
#
#
# print(os.path.exists(full_path))
#
# import shutil
#
# shutil.copy(full_path, 'new_cop.txt')

# import sys
#
# #exit(0)
#
#
# print(sys.path)

import requests

response = requests.get('https://geekbrains.ru/')

with open ('gb.html', 'w', encoding='UTF-8') as file:
    file.write(response.text)