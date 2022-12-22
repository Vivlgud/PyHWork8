from read_data import read_data

def init():
    if not (len(read_data()) > 0):
        
        with open("name.csv", 'a+') as f:
            f.write("id;surname;name;department;function\n")

        with open("adress.csv", 'a+') as f:
            f.write("id;city;street;house;apartament;other\n")

        with open("phone.csv", 'a+') as f:
            f.write("id;phone;add_phone\n")