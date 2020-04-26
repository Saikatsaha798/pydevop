
#Modules imported

import time
import sys
#Functions created

def line():
    for i in range(50):
        print("-",end="")
        time.sleep(0.01)
    print()
def arrow():
    for i in range(50):
        print(">",end="")
        time.sleep(0.02)
    print()

#Variables created

list1=['Durgapur','Waria','Andal','Kajoragram','Ukhra','Pandaveswar','Bhimgara','Panchra','Dubrajpur','Chinpai','Kachujor','Siuri']
trains=['Hool Express','Vananchal Express','Mayurakshi Fast Passenger','Black Diamond Express','Udyan Abha Toofan Express']
count=1
train=dict()
train['Hool Express']=('Durgapur','Andal','Ukhra','Pandaveswar','Dubrajpur','Siuri')
train['Vananchal Express']=('Andal','Pandaveswar','Siuri')
train['Mayurakshi Fast Passenger']=('Durgapur','Waria','Andal','Kajoragram','Ukhra','Pandaveswar','Bhimgara','Panchra','Dubrajpur','Chinpai','Kachujor','Siuri')
train['Black Diamond Express']=('Durgapur','Waria','Andal')
train['Udyan Abha Toofan Express']=('Durgapur','Andal')
timing={'up':{'Hool Express':{'Durgapur':'09:24','Andal':'09:40','Ukhra':'09:58','Pandaveswar':'10:12','Dubrajpur':'10:30','Siuri':'10:30'},'Vananchal Express':{'Andal':'01:37','Pandaveswar':'02:20','Siuri':'02:50'},'Mayurakshi Fast Passenger':{'Durgapur':'19:13','Waria':'19:23','Andal':'19:50','Kajoragram':'20:03','Ukhra':'20:13','Pandaveswar':'20:24','Bhimgara':'20:31','Panchra':'20:40','Dubrajpur':'20:47','Chinpai':'20:55','Kachujor':'21:02','Siuri':'21:14'},'Black Diamond Express':{'Durgapur':'08:57','Waria':'09:06','Andal':'09:15'},'Udyan Abha Toofan Express':{'Durgapur':'12:33','Andal':'12:48'}},'down':{'Hool Express':{'Durgapur':'15:04','Andal':'14:49','Ukhra':'14:28','Pandaveswar':'14:16','Dubrajpur':'13:56','Siuri':'13:40'},'Vananchal Express':{'Andal':'02:20','Pandaveswar':'01:27','Siuri':'00:54'},'Mayurakshi Fast Passenger':{'Durgapur':'08:20','Waria':'08:09','Andal':'07:58','Kajoragram':'07:37','Ukhra':'07:22','Pandaveswar':'07:11','Bhimgara':'07:03','Panchra':'06:55','Dubrajpur':'06:48','Chinpai':'06:39','Kachujor':'06:33','Siuri':'06:22'},'Black Diamond Express':{'Durgapur':'06:21','Waria':'06:10','Andal':'06:02'},'Udyan Abha Toofan Express':{'Durgapur':'15:49','Andal':'15:33'}}}
selection=dict()

#The heading of the project
line()
for i in range(6):
    print("-",end="")
    time.sleep(0.01)
d="TICKET BOOKING SYSTEM BY SAIKAT IS ON"
for i in d:
    print(i,end="")
    time.sleep(0.05)
for i in range(7):
    print("-",end="")
    time.sleep(0.01)
print()
line()
arrow()
arrow()
print('\n')

#Main menu of the program

c="Please Enter the Source and Destination Station from below :"
for i in c:
    print(i,end='')
    time.sleep(0.05)
print()
line()
print(list1)
line()
arrow()
print('\n')
src=input("Enter your Source Station : ")
des=input("Enter your Destination Station : ")
if src not in list1 or des not in list1:
    print('Wrong Station Selection !!!!')
    sys.exit()
    
a=list1.index(src)
b=list1.index(des)
if a<b:
    m='up'
if a>b:
    m='down'
if a==b:
    sys.exit()  
print(m)
for i in trains:
    if src in train[i] and des in train[i]:
        print(count,'. ',i,'\t\t Arriving at \t\t',timing[m][i][src])
        selection[count]=i
        count +=1
if count==1:
    print("Sorry, no train available.")
    sys.exit()

t=int(input("Please Enter the train no. you prefer : "))


c1="You have successfully selected the train   "

for i in c1:
    print(i,end='')
    time.sleep(0.05)
print(selection[t])
print()
arrow()

c2="Select your desired compartment"

for i in c2:
    print(i,end="")
    time.sleep(0.05)
print()
line()

print("1. AC\n2. Sleeper\n3. Chair Car\n4. General")

s=int(input("Input you Choice here : "))

if s!=1 and s!=2 and s!=3 and s!=4:
    print("Wrong Choice Sir !!!!!!!!")
    sys.exit()

c3="Your ticket of ",selection[t]," arriving at ",timing[m][selection[t]][src]," is booked and the bill is sent to your email with the ticket \n enjoy your ride ;))) "

for i in c3:
    print(i,end="")
    time.sleep(0.05)
print()
line()
line()







    
