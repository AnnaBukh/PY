import logging

logging.basicConfig( #  basicConfig - стандартный модуль, 
    level=logging.INFO,# в файл попадут записи с уровнем info и более высокими
    filename='c:/DEV/Python_1/HW_7_1_TEL/phonebook.log',# указывает на объект обработчика файла (имя файла в который запись идет)
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',#lineno - номер строки
    datefmt='%d.%m.%Y %H:%M:%S ',
)
