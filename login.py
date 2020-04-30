# to import os function
import os
import pickle

print("Welcome, to ABC Programme \n 1. Sign In \n 2. Sign Up")

# to get the list of directories.
l = os.listdir()

# to check whether the user file is present in the directory or not.
if 'user.dat' in l:
    c = int(input('Enter Your Choice : '))
    if c == 2:
        u = input('Enter username')
        p = input('Enter Password')
        f = open("user.dat", 'ab')
        k = [u, p]
        pickle.dump(k, f)
        f.close()
        print('Thank you, for signing up to login restart the programme ...:)')
    if c == 1:
        u = input('Enter username')
        p = input('Enter Password')
        f = open('user.dat', 'rb')
        g = pickle.load(f)
        f.close()
        if u in g:
            i = g.index(u)
            if p == g[i + 1]:
                print('Welcome', u, 'to ABC Programme')
            else:
                print('Incorrect Username and Password !!!!!')
        else:
            print('Incorrect Username and Password !!!!!')
else:
    m = open('user.dat', 'wb')
    m.close()
    c = int(input('Enter Your Choice : '))
    if c == 2:
        u = input('Enter username')
        p = input('Enter Password')
        f = open("user.dat", 'wb')
        k = [u, p]
        pickle.dump(k, f)
        f.close()
        print('Thank you, for signing up to login restart the programme ...:)')
    if c == 1:
        u = input('Enter username')
        p = input('Enter Password')
        f = open('user.dat', 'rb')
        g = pickle.load(f)
        f.close()
        if u in g:
            i = g.index(u)
            if p == g[u + 1]:
                print('Welcome', u, 'to ABC Programme')
            else:
                print('Incorrect Username and Password !!!!!')
        else:
            print('Incorrect Username and Password !!!!!')
