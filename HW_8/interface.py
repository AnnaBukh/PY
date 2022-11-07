from sys import exit 

from check import check_value
from check import get_new_personal
from check import get_inp
from check import exception_input_date

from personal_view import print_personal
from personal_view import add_record_personal
from personal_view import read_record_personal
from personal_view import change_info_personal

def info_menu():
    print(" "*5, "Вас приветствует компания")
    print("1 Показать всех сотрудников",
          "2 Найти сотрудника",
          "3 Найти отдел",
          "4 Найти профессию",
          "5 Добавить нового сотрудника",
          "6 Удалить запись о сотруднике",
          "7 Редактировать запись о сотруднике",
          "8. Выход", sep="\n")
    print()
    value_info_menu = check_value("Выберите пункт меню: ")
    return value_info_menu


def action_menu():
    while True:
        value_menu = info_menu()
        match value_menu:
            case 1:  
                print([["Номер", "ФИО", "отдел", "должность", "дата принятия на работу", "дата увольнения"]])
                print_personal()
                to_continue("Чтобы продолжить, нажмите Enter")

            case 2:  
                name_pers = search_name_pers()
                send_pers_print(name_pers)
                to_continue("Чтобы продолжить, нажмите Enter")
            case 3:  
                lst = search_by_department()
                send_pers_print(lst)
                to_continue("Чтобы продолжить, нажмите Enter")
            case 4:  
                lst = search_by_profession()
                send_pers_print(lst)
                to_continue("Чтобы продолжить, нажмите Enter")
            case 5:  
                new_record_personal = get_new_personal()
                if new_record_personal[0] != 0:
                    add_record_personal(new_record_personal[0], new_record_personal[1], new_record_personal[2],
                               new_record_personal[3], new_record_personal[4])
                    to_continue("Чтобы продолжить, нажмите Enter")
                else:
                    to_continue("Чтобы продолжить, нажмите Enter")
            case 6: 
                menu_del_info()
                to_continue("Чтобы продолжить, нажмите Enter")
            case 7:  
                menu_change_info()
                to_continue("Чтобы продолжить, нажмите Enter")
            case 8:  
                exit("Программа выполнена")


def search_name_pers():
    name_person = get_inp("Введите ФИО: ")
    data = read_record_personal()
    if data[0] == 0:
        return ""
    name_person_search = []
    for i in data:
        if i[1] == name_person:
            name_person_search.append(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}")
    if len(name_person_search) > 0:
        return name_person_search
    else:
        return ["Сотрудника не существует"]

def send_pers_print(value):
    for i in value:
        print(i)

def search_by_department():
    department_person = get_inp("Введите отдел: ")
    data = read_record_personal()
    if data[0] == 0:
        return ""
    department_person_search = []
    for i in data:
        if i[2] == department_person:
            department_person_search.append(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}")
    if len(department_person_search) > 0:
        return department_person_search
    else:
        return ["Отдела не существует"]


def search_by_profession():
    prof_person = get_inp("Введите должность: ")
    data = read_record_personal()
    if data[0] == 0:
        return ""
    prof_person_search = []
    for i in data:
        if i[3] == prof_person:
             prof_person_search.append(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}")
    if len(prof_person_search) > 0:
        return  prof_person_search
    else:
        return ["Должность не существует"]


def menu_change_info():
    id_number = input("Введите номер записи,которую необходимо редактировать:  ")
    data = read_record_personal()
    if data[0] == 0:
        return ""
    for i in data:
        if i[0] == id_number:
            print(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}")
            id, name_personal, department, profession, date_employment, date_dismissal = i
            break
    else:
        return "The service number is missing!"
    print("1 ФИО", "2 отдел", "3 должность", "4 дата принятия на работу", "5 дата увольнения", "6 вернуться в основное меню",  sep="\n")
    num = check_value("\n Выберите пункт для корректировки: ")
    match num:
        case 1:
            name_personal = get_inp('Введите ФИО: ')
            to_continue("Чтобы продолжить, нажмите Enter")
        case 2:
            department = get_inp('Введите отдел: ')
            to_continue("Чтобы продолжить, нажмите Enter")
        case 3:
            profession = get_inp('Ыыедите должность: ')
            to_continue("Чтобы продолжить, нажмите Enter")
        case 4:
            date_employment = exception_input_date('Введите дату принятия на работу: ')
            to_continue("Чтобы продолжить, нажмите Enter")
        case 5:
            date_dismissal = exception_input_date('Введите дату увольнения: ')
            to_continue("Чтобы продолжить, нажмите Enter")
        case _:
            print()
    change_info_personal(id, name_personal, department,
                     profession, date_employment, date_dismissal)


def menu_del_info():
    id_number = input("Введите номер записи,которую необходимо удалить:  ")
    data = read_record_personal()
    if data[0] == 0:
        return "Такой записи не существует"
    for i in data:
        if i[0] == id_number:
            print(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}")
            id, name_personal,  department, profession, date_employment, date_dismissal = i
            break
    name_personal = " "
    department = " "
    profession = " "
    date_employment = " "
    date_dismissal = " "
    change_info_personal(id, name_personal, department,
                     profession, date_employment, date_dismissal)


def to_continue(messege):
    input(messege)