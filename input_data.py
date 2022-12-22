from write_data import count_data

def input_data():
    """Ввод данных
    
    Returns: Dict - словарь для записи в файлы базы"""

    dct = dict()
    Id = count_data("name.csv") 
    dct["id"] = Id     
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["department"] = input('Введите Отдел: ')
    dct["function"] = input('Введите Должность: ')
    dct["phone"] = input('Введите Номер основного телефона: ')
    dct["add_phone"] = input('Введите Номер дополнительного телефона: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartament"] = input('Введите Квартира: ')
    dct["other"] = input('Введите Комментарий: ')
    return dct