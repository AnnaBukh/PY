# 3. Написать функцию - аргументы имена сотрудников, 
# возвращает  - словарь,
#  ключи — первые буквы имён,
#  значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

# сначала сортировка, потом собираем в словарь

# from tkinter.font import names

# def list_names(kol: int):
#     names = tuple()
#     for i in range(kol):
#         line = tuple(input("Enter the name of the list: "))
#         names.append("".join(line))
#     return names

# kol =int(input("Enter the numbers of names: "))

# names = []
# for i in range(kol):
#     line = str(input("Enter the name of the list: "))
#     names.append("".join(line))
# names = " , ".join(names)

# print(names)

# list_name = list_names(int(input("Enter the numbers of names: ")))
# print(list_name)

# print(type(list_name))

# def dictionary_names(*names):
#     dict_names = {}
#     for i in sorted(names):
#         key = i[0]
#         if key in dict_names:
#             dict_names[key] += [i]
#         else:
#             dict_names[key] = [i]

#     return dict_names


def dictionary_names(*names):
    dict_names = {}
    for i in names:
        key = i[0]
        if key in dict_names:
            dict_names[key].append(i)
        else:
            dict_names[key] = [i]

    return dict_names

print(dictionary_names("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))
