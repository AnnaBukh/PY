# Задайте список из n чисел, заполненный по формуле (1+1/n)**n и выведите на экран их сумму
n = int(input())
my_list = []
for k in range(1, n + 1):
    my_list.append(round((1+1/k)**k, 0)) 
print(my_list)
summ = 0
for k in range(n):
    summ = summ + my_list[k]
print(summ)