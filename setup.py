import mysql.connector
import os
import pickle

setupcommand = ['create database school;',
                'use school;',
                'create table student('
                'adm_no int(6) not null primary key,'
                'name varchar(30) not null,'
                'class int(2) not null,'
                'Section varchar(30) not null,'
                'attendance int(3) not null,'
                'english int(3) not null,'
                'bengali_or_hindi int(3) not null,'
                'science int(3) not null,'
                'social_science int(3) not null,'
                'maths int(3) not null);']

def setup():
    global c
    host = str(input('Enter the Host      (DataBase)  = '))
    user = str(input('Enter the User      (DataBase)  = '))
    password = str(input('Enter the Password  (DataBase)  = '))
    con = mysql.connector.connect(host=host, user=user, password=password)
    print('It\'s time you setup a username and password !!!')
    u = str(input('Enter your Username : '))
    p = str(input('Enter your Password : '))
    with open('../School Management system GUI/data.dat', 'wb+') as fw:
        pickle.dump([host, user, password, u, p], fw)
    c = con.cursor()
    for cmd in setupcommand:
        c.execute(cmd)
    print('Installation completed !, now you can run the main program !!!!!')

try:
    if 'data.dat' in os.listdir():
        with open('../School Management system GUI/data.dat', 'rb+') as fr:
            a = pickle.load(fr)
        print('You previously installed this, don\'t this try again !!!!!!')

    else:
        setup()

except mysql.connector.errors.InterfaceError:
    print('Your host that is mention, is not there make sure to check it next time !!!!')

except mysql.connector.errors.ProgrammingError:
    print('Make sure to enter the correct username and password, next time !!!!')

except mysql.connector.errors.DatabaseError:
    try:
        for cmd in setupcommand:
            if setupcommand.index(cmd) != 0:
                c.execute(cmd)
        print('Installation completed !, now you can run the main program !!!!!')
    except mysql.connector.errors.ProgrammingError:
        print('Installation completed !, now you can run the main program !!!!!')

finally:
    print('Have a good day !! :)')