

def check_value(message) -> int:
    while True:
        value = input(message)
        if value.isdigit() and (int(value) in [1, 2, 3, 4, 5, 6, 7, 8]):
            return int(value)
        else:
            print("\n","Некорректный ввод, повторите","\n")


def get_new_personal():
    while True:
        name_personal = input("Введите ФИО: ")
        if exception_input(name_personal):
            break
        else:
            print("\n", "Некорректно введены данные, попробуйте заново", "\n")
    while True:
        department = input("Введите отдел: ")
        if exception_input(department):
            break
        else:
            print("\n", "Некорректно введены данные, попробуйте заново", "\n")
    while True:
        profession = input("Введите должность: ")
        if exception_input(profession):
            break
        else:
            print("\n", "Некорректно введены данные, попробуйте заново", "\n")
    while True:
        date_employment = input("Дата принятия на работу: ")
        if exception_input_date(date_employment):
            break
        else:
            print("\n", "Некорректно введены данные, попробуйте заново", "\n")
    while True:
        date_dismissal = input("Дата увольнения (введите 0, если все еще работает): ")
        if exception_input_date(date_dismissal):
            break
        else:
            print("\n", "Некорректно введены данные, попробуйте заново", "\n")
    
    res = [name_personal, department, profession, date_employment, date_dismissal]
    return res


def get_inp(message):
    while True:
        value = input(message)
        if exception_input(value):
            return value
        else:
            print("\n", "Некорректно введены данные, попробуйте заново", "\n")

def exception_input(name_p):
    for i in "!@#$%^&/*?<>1234567890'\"":
            if name_p.find(i)>=0: # строковый метод нахождения совпадения подстроки в строке, возвращает "-1"
               return False
    else:
        return True

def exception_input_date(date_p):
    date_p = date_p.replace(" ", '').replace(".", '')
    if date_p=="0":
        return True
    if date_p.isdigit():
        if 0<int(date_p[:2])<32 and 0<int(date_p[2:4])<13 and 2000<int(date_p[4:])<2022:
            return True
    else: 
        return False

