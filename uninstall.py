import mysql.connector
import pickle
import os

try:
    with open('../School Management system GUI/data.dat', 'rb+') as fr:
        a = pickle.load(fr)
    host, user, password = a[0], a[1], a[2]
    con = mysql.connector.connect(host=host, user=user, password=password)
    c = con.cursor()
    c.execute('drop database school;')
    os.remove('../School Management system GUI/data.dat')
    print('Uninstalled this!, you are good to go !!!!')

except FileNotFoundError or mysql.connector.ProgrammingError:
    print('Due to some manipulations, our connections are failing, so try reinstalling !!!!!')

finally:
    print('Have a good day !! :)')