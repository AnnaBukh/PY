# Вычислить число c заданной точностью d
# модуль decimal
# решение должно быть через функцию

from decimal import Decimal 

num_float = float(input("Введите число: "))
d_round = float(input("Введите точность округления числа в формате 0.00001: "))

def round_number(number, d):
    number_1 = Decimal(f"{number}")
    number_1 = number_1.quantize(Decimal(f"{d}"))
    return number_1

print(round_number(num_float, d_round))

