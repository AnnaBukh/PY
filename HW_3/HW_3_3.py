# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования 
# встроенной функции преобразования, без строк.

number = int(input())

def convert_10_to_2(num):
    num_to_2 = ""
    while num != 0:
        num_to_2 = str(num % 2) + num_to_2
        num //= 2
    return (num_to_2)

num_2 = convert_10_to_2(number)
print(num_2)