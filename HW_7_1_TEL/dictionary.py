import logger as log
import csv # cvs  - встроенная бибилиотека, только импорт

phonebook = []

# 1 Вывести все записи

def all_record():
    all_record_row = []
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', encoding='utf-8') as file:
        all_record_row = csv.reader(file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        arrive = []
        for row in all_record_row:
            arrive.append(row)
            # print(row)
        return arrive

# 2 Найти номер телефона по владельцу телефона
def search_name(name=''):
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', encoding='utf-8') as file:
        arrive = csv.reader(file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        result = []
        for row in arrive:
            if name == row[0]:
                result.append(row[1])
        if len(result) == 0:
            # print(f'Контакты не найдены')
           return f'Владельца номера телефона в книге не существует'
        else:
            # print(result)
            return(result)
           
# 3 Найти владельца по номеру телефона
def search_tel(num=''):
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', encoding='utf-8') as file:
        arrive = csv.reader(file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        result = []
        for row in arrive:
            if num in row[1]:
                result.append(row[0])
        if len(result) == 0:
           return f'Номера телефона в книге не существует'
        else:
            return(result)

# 4 Добавить запись 

# base = {}
# def new_record(key, value):
#     with open('c:/DEV/Python/HW_7_1_TEL/phonebook.txt', 'a', encoding='utf-8') as file:
#         # key = input("Введите Имя Фамилию Отчество: ")
#         # value = input("Введите номер телефона: ")
#         # name == key
#         # num = value
#         base[key] = value
#         file.write(f'{key} : {value}')
#     return base

def new_record(name='', num=''):
    global phonebook
    new_record = [name.title(), num]
    phonebook.append(new_record)
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(new_record)
 
   
# 6_1 Удалить запись с поиском по владельцу телефона
# алгоритм: открыть файл, записать данные , кроме тех, которые хотим удалить в массив, из массива перезаписать данные в тот же файл
def delete_name(name=''):
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'r', newline='', encoding='utf-8') as in_file:
        array = []
        reader = csv.reader(in_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if name != row[0]:
                array.append(row)
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in array:
            writer.writerow(row)

# 6_2 Удалить запись с поиском по номеру телефона
# алгоритм: открыть файл, записать данные , кроме тех, которые хотим удалить в массив, из массива перезаписать данные в тот же файл
def delete_num(num=''):
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'r', newline='', encoding='utf-8') as in_file:
        array = []
        reader = csv.reader(in_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if num not in row[1]: 
                array.append(row)
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in array:
            writer.writerow(row)

# 5_1 Редактировать владельца телефона

def change_name(name='', new_name=''):
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'r', newline='', encoding='utf-8') as in_file:
        array = []
        reader = csv.reader(in_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if name != row[0]:
                array.append(row)
            else:
                row[0] = new_name.title()
                array.append(row)
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in array:
            writer.writerow(row)

# 5_2 Редактировать номер телефона

def change_num(num='', new_num=''):
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'r', newline='', encoding='utf-8') as in_file:
        array = []
        reader = csv.reader(in_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if num not in row[1]:
                array.append(row)
            else:
                row[1] = new_num.title()
                array.append(row)
    with open('c:/DEV/Python_1/HW_7_1_TEL/phonebook.csv', 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in array:
            writer.writerow(row)