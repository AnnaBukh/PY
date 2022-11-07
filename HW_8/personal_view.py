from os import path


def print_personal():
    if path.isfile("staff.csv"):
        with open('staff.csv', 'r', encoding="utf-8") as file:
            [print(i.replace("\n", '')[:-1].split(";"))
             for i in file.readlines()]
            print()
        return 1
    else:
        print("Файл не найден")
        return 0


def add_record_personal(name_personal, department, profession, date_employment, date_dismissal):
    if not path.isfile("staff.csv"):
        print("Файл staff.csv не найден, создайте новый файл staff.csv")
    with open('c:\DEV\Python\Lesson_8\end_id.txt', 'r+', encoding="utf-8") as file_id:
        data = file_id.readlines()
        print(data)
        id = str(int(data[0].replace("\n", ""))+1)
        file_id.seek(0)# устанавливает текущую позицию, сместить в начало
        file_id.write(id+"\n")
    with open('staff.csv', 'a', encoding="utf-8") as file:
        file.write('\n{0};{1};{2};{3};{4};{5};'.format(id, name_personal, department, profession, date_employment, date_dismissal))
        print("Запись добавлена в staff.csv.csv")

def read_record_personal() -> list[str]:
    if path.isfile("staff.csv"):
        data = []
        with open('staff.csv', 'r', encoding="utf-8") as file:
            data = [(i.replace("\n", '')[:-1].split(";"))
                    for i in file.readlines()]
        return data
    else:
        print("Файл не найден")
        return [0]


def change_info_personal(id: str, name_personal, department, profession, date_employment, date_dismissal):
    new_str = '{0};{1};{2};{3};{4};{5};\n'.format(id, name_personal, department, profession, date_employment, date_dismissal)
    if path.isfile("staff.csv"):
        with open('staff.csv', 'r', encoding="utf-8") as file1:
            data = file1.readlines()
            for i in range(len(data)):
                lst = data[i].replace("\n", "")[:-1].split(';')
                if lst[0] == id:
                    data[i] = new_str
                    break
        with open('staff.csv', 'w', encoding="utf-8") as file2:   
            file2.writelines(data)    
        print("Запись добавлена в файл staff.csv.csv")
    else:
        print("Файл не найден")
        return 0



