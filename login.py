# to import os function
import os

print("Welcome, to ABC Programme \n 1. Sign In \n 2. Sign Up")

# to get the list of directories.
l=os.listdir()

# to check whether the user file is present in the directory or not.
if 'user.txt' in l:
    c=int(input('Enter Your Choice : '))
    if c==2:
        u=input('Enter username')
        p=input('Enter Password')
        f=open("user.txt",'a')
        f.write(u+','+p+',')
        f.close()
        print('Thank you, for signing up to login restart the programme ...:)')
    if c==1:
        u = input('Enter username')
        p = input('Enter Password')
        f=open('user.txt','r')
        g=f.read()
        t=g.split(',')
        f.close()
        if u and p in t:
            print('Welcome', u, 'to ABC Programme')
        else:
            print('Incorrect Username and Password !!!!!')
else:
    m=open('user.txt','w')
    m.close()
    c = int(input('Enter Your Choice : '))
    if c == 2:
        u = input('Enter username')
        p = input('Enter Password')
        f = open("user.txt", 'a')
        f.write(u + ',' + p + ',')
        f.close()
        print('Thank you, for signing up to login restart the programme ...:)')
    if c == 1:
        u = input('Enter username')
        p = input('Enter Password')
        f = open('user.txt', 'r')
        g = f.read()
        t = g.split(',')
        f.close()
    if u and p in t:
        print('Welcome', u, 'to ABC Programme')
    else:
        print('Incorrect Username and Password !!!!!')
