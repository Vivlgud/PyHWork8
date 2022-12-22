def print_data(data, search = False):
    """Вывод в консоль информации из базы"""
    if len(data) > 0:
        print("id".center(2), "Фамилия".center(15), "Имя".center(10), "Отдел".center(10), "Должность".center(10),\
           "Телефон".center(13), "Доп.телефон".center(13),\
            "Город".center(10), "Улица".center(10), "Дом".center(3), "Квартира".center(3), "Коммент.".center(15))
        print("-"*125)

        if not search:
            del data[0]
        for item in data:          
            print(item[0].center(2), item[1].center(15), item[2].center(10), item[3].center(10), item[4].center(10),\
           item[5].center(13), item[6].center(13),\
            item[7].center(10), item[8].center(10), item[9].center(3), item[10].center(3), item[11].center(15))
    else:
        print("\n")
        print("*"*120 + "\nСправочник пуст!\n" + "*"*120)
        print("\n")