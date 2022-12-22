from push_data import *
from read_data import *
from print_data import *
from search_data import *


def start():
    """Выбор раздела базы данных"""
    
    print()
    print("Операции по работе с базой сотрудников:\n\
    1 - Вывести всю информацию из базы;\n\
    2 - Добавить сотрудника;\n\
    3 - Поиск информации о сотруднике;\n\
    0 - Завершение работы")
    ch = input("Введите пункт меню: ")
    while True:
        if ch == '1':
            data = read_data()
            print()
            print_data(data)
            start()
        elif ch == '2':
            push_data()
            start()
        elif ch == '3':
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены")                
            start()
        elif ch == '0':
            print("Работа с базой завершена")
            raise SystemExit
        else:
            print("Вы ошиблись! Введите повторно пункт меню")
            start()