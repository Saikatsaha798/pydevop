import time
import os

def line():
    for i in range(50):
        print("-", end="")
        time.sleep(0.01)
    print()

line()

d = "Data Handler +"
for i in d:
    print(i, end="")
    time.sleep(0.05)
print()

line()

print(
    'Actions offered : \n 1. Create a File \n 2. Input data in a File \n 3. Move File \n 4. Copy File \n 5. Rename '
    'File \n 6. Capitalize \n 7. Inverse Capitalize \n '
    '8. Delete File ')

c = int(input('Enter Your Choice : '))

if c == 1:
    f = input('Enter the path of the file (with "\\")')
    f1 = open(f, 'w')
    f1.close()

elif c == 2:
    f = input('Enter the path of the file (with "\\") ')
    d = input('Enter the data is to be saved in the file')
    f1 = open(f, 'a')
    f1.write(d)
    f1.close()

elif c == 3:
    src = input('Enter the Initial Path of the file (with "\\") ')
    des = input('Enter the Destination Path of the file (with "\\") ')
    fi = open(src, 'r')
    fd = open(des, 'w')
    fd.close()
    fd = open(des, 'a')
    while True:
        l = fi.readline()
        fd.write(l)
        if l == '':
            break
    fi.close()
    fd.close()
    os.remove(src)

elif c == 4:
    src = input('Enter the Initial Path of the file (with "\\") ')
    des = input('Enter the Destination Path of the file (with "\\") ')
    fi = open(src, 'r')
    fd = open(des, 'w')
    fd.close()
    fd = open(des, 'a')
    while True:
        l = fi.readline()
        fd.write(l)
        if l == '':
            break
    fi.close()
    fd.close()

elif c == 5:
    src = input('Enter the Initial Path of the file (with "\\") ')
    des = input('Enter the Destination Path of the file (with "\\") ')
    fi = open(src, 'r')
    fd = open(des, 'w')
    fd.close()
    fd = open(des, 'a')
    while True:
        l = fi.readline()
        fd.write(l)
        if l == '':
            break
    fd.close()
    fi.close()
    os.remove(src)
elif c == 6:
    w = ''
    f = input('Enter the Path of the file (with "\\") ')
    f1 = open(f, 'r')
    g = f1.readlines()
    for i in g:
        j = i.split()
        for k in j:
            w += k.upper()
    f1.close()
    f1 = open(f, 'w')
    f1.write(w)
    f1.close()

elif c == 7:
    w = ''
    f = input('Enter the Path of the file (with "\\") ')
    f1 = open(f, 'r')
    g = f1.readlines()
    for i in g:
        w += i.lower()
    f1.close()
    f1 = open(f, 'w')
    f1.write(w)
    f1.close()

elif c == 8:
    f = input('Enter the path of the file (with "\\")')
    os.remove(f)
else:
    print('Please enter a valid choice !!!!!')
