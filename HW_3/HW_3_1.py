#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22


number = int(input())
from random import randrange
def list_rand(num):
    line_1 = []
    for i in range(1, num + 1):
        line_1.append(randrange(0, 10)) 
    return(line_1)
line_2 = list_rand(number)
print(line_2)
def find_sum_el_even_position(line):
    summa = 0
    for i in range(1, len(line), 2):
        summa += line[i]
    print(summa)
find_sum_el_even_position(line_2)