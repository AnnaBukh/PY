# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
from random import randrange
number = int(input())


def list_rand(num):
    line_1 = []
    for i in range(1, num + 1):
        line_1.append(randrange(0, 10))
    return (line_1)


line_2 = list_rand(number)
print(line_2)


def product_of_pair(line, num):

    product_1 = []
    product_2 = []
    length_line_1 = len(line)

    if length_line_1 % 2 == 0:
     for i in range(length_line_1):
        while i < length_line_1/2 and num > length_line_1/2:
            num = num  - 1
            product_1.append(line[i]*line[num])
            i += 1
    # if length_line_1 % 2 == 0:
    # for i in range(0, length_line_1 // 2):
    #     product_1.append(line[i]*line[length_line_1 - i - 1])
     return (product_1)

    elif length_line_1 % 2 != 0:
        for i in range(0, round(length_line_1 // 2)):
         product_2.append(line[i]*line[length_line_1 - i - 1])
    product_2.append(line[round(length_line_1 // 2)])
    return(product_2)

line_3 = product_of_pair(line_2, number)
print(line_3)
