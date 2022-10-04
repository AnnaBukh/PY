# напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
# заполненных числами из промежутка [-N;N]. Найдите произведение элементов на указанных позициях
position_1 = int(input("Position one: "))
position_2 = int(input("Position two: "))
n = int(input("Number of elements: "))
if (position_1) > (n * 2 + 1) or (position_1) <= 0:
    print("Position one incorrect ")
elif (position_2) > (n * 2 + 1) or (position_2) <= 0:
    print("Position two incorrect ")
else:
 my_list = []
 for k in range(-(n + 1), n, 1):
    my_list.append(k+1)
 print(my_list)
 result =  my_list[position_1 - 1]*my_list[position_2 - 1]
 print(result)