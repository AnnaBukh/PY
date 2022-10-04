# напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

num_float = float(input())
length_num = len(str(num_float))
num_int = int(num_float*10**(length_num-2))
#print(num_int)
if num_int < 0:
    num_int *= (-1)
#print(num_int)
summ = 0 
for i in range (length_num + 1):
    summ = summ + num_int % 10
    num_int = num_int // 10
print(summ)
 