from read_data import*
from print_data import*

def search_data(word, data):
    """Поиск по любому слову из базы"""
    if len(data) > 0:
        lst = []
        for item in data:
            if word in item:
                lst.append(item)
        if lst == []:
            return None
        else:
            return lst
    else:
        return None