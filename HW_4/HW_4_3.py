# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# set (с упорядочиванием), dictionary, задача решается через цикл

from random import randrange 

number = int(input())

def list_rand(num): # метод из домашней задачи 3.2 
    line_1 = []
    for i in range(1, num + 1):
        line_1.append(randrange(0, 10)) 
    return(line_1)

line_2 = list_rand(number)
print(line_2)

def unique_number(line_number):
    line_3_dict = dict.fromkeys(line_number, 0) # преобразование списка в словарь, ключ - число из списка, значение его - ноль
    # print(line_3_dict) # исходный словарь
    for i in line_number:# идем по списку
         line_3_dict[i] +=1 # увеличиваем значение ключа с нуля исходного на кол-во повторяющегося числа по списку(ключа)
    # print(line_3_dict)# подсчет кол-ва повторяющихся ключей
    line_3 = []# список для записи в него неповторяющихся ключей
    for key in line_3_dict:
        if line_3_dict[key] == 1: #  если значение больше не повторяется,
            line_3.append(key)# в список новый добавляем ключ 
    return line_3

print(unique_number(line_2))
