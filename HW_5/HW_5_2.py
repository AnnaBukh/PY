
# проверка exists - проверка существования файла
# модуль itertools
# кодирование groupby
# декодирование starmap
# две функции  - кодирование + декодирование, в файле Nнное количество строк 

#2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby
import os.path 
from re import I
from itertools import starmap

# # функция создания файла 
# def new_file(name_file):
#     my_file = open(name_file, 'w', encoding = 'utf-8')
#     my_file.close()

# new_file(input("Enter the name of the file: "))

# # функция записи исходного текста в исходный файл  
# def text_file(name_file, text):
#     if os.path.exists(name_file):
#         with open(name_file, "a", encoding = 'utf-8') as my_file:
#             my_file.write(text)
#     else:
#         print("Incorrect file name to record text")

# text_file(input("Enter the name of the file: "), input("Enter the text to record: "))

#  функция кодирования текста для записи методом groupby

# def groupby_text(text):
#     for char, same in groupby(text):
#         count = sum(1 for _ in same)
#         yield char if count == 1 else str(count)+char
#     return text

# print(''.join(groupby_text("aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa")))

# data  = "aaaaavvvvvvvvvvvccc"
# groups = []
# data = sorted(data)
# for k, g in groupby(data):# Сохранение группового итератора в виде списка
#     groups.append(list(g))
# print(data)
# print(k)
# print(len(list(g)))

#starmap
# itertools.starmap(function, iterable)
# Функция starmap() модуля itertools создает итератор, который вычисляет функцию function, 
# используя аргументы, полученные из кортежей в итерируемой последовательности iterable.
# Используется вместо map(), когда параметры функции уже сгруппированы в кортежи из одной 
# итерации, т. е. данные были предварительно упакованы в кортежи.


def text_code(name_file = "text_words.txt", name_code_file = "text_code_words.txt"):
    if os.path.exists(name_file) and not os.path.exists(name_code_file):
        with open(name_file) as my_file_1, open(name_code_file, "a", encoding = 'utf-8') as my_file_2:
            for i in my_file_1:
                my_file_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The file do not exist in the system!")


def text_decode(name_decode_file):
    if os.path.exists(name_decode_file):
        with open(name_decode_file) as my_file:
            n = ""
            for k in my_file:
                word_num = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_num.append([int(n), i])
                        n = ""
                return("".join(starmap(lambda x, y: x * y, word_num)))
    else:
        print("The file do not exist in the system!")

text_code(input("Enter the name of the file: "), input("Enter the file name to record: "))

text_decode(input("Enter the name of the file to decode: "))