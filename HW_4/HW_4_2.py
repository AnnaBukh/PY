#  Задайте натуральное число N. 
#  Напишите программу, которая составит список простых множителей числа N.
# использовать сущ алгоритм
# возвращается список 

number_N = int(input("Введите натуральное число: "))

def prime_factors(number):
 list_1 = []
 fact_min = 2
 while fact_min <= number:
    if number % fact_min == 0:
        list_1.append(fact_min)
        number //= fact_min
    else:
        fact_min +=1
 return list_1

print(prime_factors(number_N))