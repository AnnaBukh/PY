# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

from random import sample


def get_list(size, max_num): # создали список 
    return sample(range(20, max_num), size)

size_list = int(input("Enter the size of the list: "))
num_max = int(input("Enter maximum number of the list: "))
list_1 = get_list(size_list, num_max)
print(list_1)

# list_1 = [20, 21, 40, 42, 60, 63, 80, 84, 100, 20, 21, 40, 41, 42]

def get_list_divisible_20_21(new_list):
    # list_max_next = [new_list[i] for i in range(len(new_list)) \
    #     if new_list[i] % 20 == 0 or new_list[i] % 21 == 0]
    list_max_next = [new_list[i] for i in range(len(new_list)) \
        if not new_list[i] % 20 or not new_list[i] % 21]
    return list_max_next

print(get_list_divisible_20_21(list_1))