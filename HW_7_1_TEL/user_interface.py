# import data_provide as dp
import dictionary as dic
import logger as log

# def сheck_num(menu_item): # проверка корректности введенных данных
#     # while arg.isdigit() != True:
#     if (menu_item.isdigit()!= True) or (int(menu_item) >= 8):
#         log.logging.info('Пользователь ввел некорректные данные: {menu_item}')
#         print('\nВведите корректный пункт меню')
#         menu_item = input('Введите корректный пункт меню: ')
#     return int(menu_item)


def menu():
    while True:
        print('\nМЕНЮ')
        print('1 Показать весь справочник')
        print('2 Найти запись по владельцу')
        print('3 Найти запись по номеру телефона')
        print('4 Добавить запись')
        print('5 Редактировать запись')
        print('6 Удалить запись')
        print('7 Закрыть справочник\n')
        # number = сheck_num(input('Выберите пункт меню: '))
        number = int(input('Выберите пункт меню: '))

        if number == 1:
            log.logging.info('User select item menu: 1')# запись в журнал событий
            # dic.all_record()# вывести все записи на экран
            print(dic.all_record())

        elif number == 2:
            log.logging.info('User select item menu: 2')
            search = input('Введите владельца телефона: ')
            log.logging.info(f'User enter: {search}')
            print(dic.search_name(name=search))

        elif number == 3:
            log.logging.info('User select item menu: 3')
            search = str(input('Введите номер телефона: '))
            log.logging.info(f'User entered: {search}')
            print(dic.search_tel(num=search))

        elif number == 4:
            log.logging.info('User select item menu: 4')
            name = input("Введите владельца номера телефона: ")
            num = input("Введите номер телефона: ")
            log.logging.info('User add new record')
            dic.new_record(name, num)

        elif number == 5:
            log.logging.info('User select item menu: 5')
            print('1 Изменить запись о владельце телефона: ')
            print('2 Изменить номер телефона: ')
            number_5 = int(input('Выберите пункт меню: '))

            if number_5 == 1:
                log.logging.info('User select item menu: 6_1')
                search = input('Введите владельца телефона: ')
                log.logging.info(f'User entered: {search}')
                search_new_name = input('Введите нового владельца телефона: ')
                dic.change_name(name=search, new_name=search_new_name)

            if number_5 == 2:
                log.logging.info('User select item menu: 6_2')
                search = str(input('Введите номер телефона из книги: '))
                log.logging.info(f'User entered: {search}')
                search_new_num = input('Введите нового владельца телефона: ')
                dic.change_num(num=search, new_num=search_new_num)


        elif number == 6:
            log.logging.info('User select item menu: 6')
            print('1 Удалить запись с поиском по владельцу')
            print('2 Удалить запись с номером телефона')
            number_6 = int(input('Выберите пункт меню: '))

            if number_6 == 1:
                log.logging.info('User select item menu: 6_1')
                search = input('Введите владельца телефона: ')
                log.logging.info(f'User entered: {search}')
                dic.delete_name(name=search)

            if number_6 == 2:
                log.logging.info('User select item menu: 6_2')
                search = str(input('Введите номер телефона: '))
                log.logging.info(f'User entered: {search}')
                dic.delete_num(num=search)

        elif number == 7:
            log.logging.info('End')
            print('Справочник закрыт')
            break

        else:
            log.logging.info(f'User entered an invalid menu value: {number}')
            print('\nВведите корректный пункт меню')


