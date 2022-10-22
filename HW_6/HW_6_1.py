#  Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
#  предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# не должно быть первого элемента
# решение в сроку, обернутую в функцию

from random import choices

def get_list(size): # создали список 
    return choices(range(size*2), k = size)

size_list = int(input("Enter the size of the list: "))
list_1 = get_list(size_list)
print(list_1)

# list_1 = [15, 16, 2, 3, 1, 7, 5, 4, 10]

def get_list_max_next(new_list):
    # list_max_next = []
    # for i in range(len(new_list) - 1):
    #     if new_list[i] < new_list[i + 1]:
    #         list_max_next.append(new_list[i + 1])
    list_max_next = [new_list[i  + 1] for i in range(len(new_list)-1) if new_list[i] < new_list[i + 1]]
    return list_max_next

# print(get_list_max_next(get_list(size_list)))

print(get_list_max_next(list_1))