def read_data():
    """ чтение данных из файлов базы и объединение их в один список"""
    lst_name = []
    with open('name.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_name.append(temp)
        
    lst_adress = []
    with open('adress.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_adress.append(temp)
       

    lst_ph = []
    with open('phone.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_ph.append(temp)
        

    lst = []
    for i in range(len(lst_name)):
        lst.append([lst_name[i][0], lst_name[i][1], lst_name[i][2], lst_name[i][3], lst_name[i][4], \
            lst_ph[i][1], lst_ph[i][2], \
            lst_adress[i][1], lst_adress[i][2], lst_adress[i][3], lst_adress[i][4], lst_adress[i][5]])
    return lst