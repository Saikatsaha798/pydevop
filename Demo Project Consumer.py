"""
PIP:
pip install mysql
pip install mysqlclient
pip install mysql-connector-python
pip install --only-binary :all: mysqlclient
pip install prettytable

SQL:
1. Create database DotPy
2. Database: use DotPy
3. The Consumer Table:
create table consumer(c_id varchar(10),cons_name varchar(30),address varchar(30),s_id varchar(8))
"""
#==================DotPy Consumer Database===================
import time
import MySQLdb
from prettytable import PrettyTable
def line():
    for i in range(50):
               print("-",end="")
               time.sleep(0.01)
    print()
def arrow():
    for i in range(10):
               print(" >  ",end="")
               time.sleep(0.02)
    print()
db = MySQLdb.connect("localhost","root","1234","DotPy" )
cur = db.cursor()
project_name="DotPy Consumer Database"
for i in range(10):
            print(" >  ",end="")
            time.sleep(0.02)
print("Project Started ",end="")
arrow()
for i in range(100):
               print("-",end="")
               time.sleep(0.02)
print()
line()
for i in project_name:
               print(i,end="")
               time.sleep(0.02)
print()
line()
#------------------------------Program Started->Dotpy Consumer Database Main Menu-----------------------------
while True:
    #line()
    print("**************Consumer Database Main Menu**************")
    line()
    print("|           1=>Add record        |")
    print("|           2=>Delete            |")
    print("|           3=>Edit /Update      |")
    print("|           4=>Diplay            |")
    print("|           5=>Exit              |")
    line()
    m=int(input("Select task (1 to 5) : "))
    #-----------------------------Main Menu Choice 1 Insert Record----------------------------------------
    if m==1:
        v1=input("Enter C_id: ")
        v2=input("Enter Cons_name: ")
        v3=input("Enter Address: ")
        v4=input("Enter S_id: ")
        sql='insert into consumer values("%s","%s","%s","%s")'%(v1,v2,v3,v4)
        cur.execute(sql)
        db.commit()
        print("Information Added To Database Successfully")
        arrow()
    #--------------------------------Main Menu Choice 2 Delete Sub Menu-------------------------------------
    elif m==2:
        while True:
            line()
            print(" ************** Delete Sub Menu **************")
            line()
            print("| 0=> Delete All Record                |")
            print("| 1=> Delete by : c_id                 |")
            print("| 2=> Delete by : cons_name            |")
            print("| 3=> Delete by : address              |")
            print("| 4=> Delete by : s_id                 |")
            print("| 5=> Exit to Main Menu                |")
            line()
            d=int(input("Enter Your Choice (1 to 5):"))
             #--------------------------Delete Sub Menu choice 0 All record------------------------
            if d==0:
                print("Data in Your table is :")
                line()
                cur.execute('select *from consumer')
                rows=cur.fetchall()
                t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                for x,y,z,a in rows:
                    t.add_row([x,y,z,a])
                print(t)
                line()  
                rows=cur.fetchall()
                print(rows)
                line()
                ch=input("You Want to Delete (Y/N):")
                if ch=='y' or ch=='Y':
                    cur.execute('delete from consumer')
                    db.commit()
                    print ("=====>  DATA REMOVED  <=====")
                    arrow()
                else:
                    print("Continue.....")
                    arrow()
            #--------------------------Delete Sub Menu choice 1 by c_id------------------------
            if d==1:
                print("Data in Your table is :")
                line()
                cur.execute('select *from consumer')
                rows=cur.fetchall()
                t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                for x,y,z,a in rows:
                    t.add_row([x,y,z,a])
                print(t)
                line()
                c=input("Enter c_id for delete record : ")
                cur.execute("select *from consumer where c_id='%s' "%c)
                rows=cur.fetchall()
                print(rows)
                line()
                ch=input("You Want to Delete (Y/N):")
                if ch=='y' or ch=='Y':
                    cur.execute("delete from consumer where c_id='%s' "%c)
                    db.commit()
                    print ("=====>  DATA REMOVED  <=====")
                    arrow()
                else:
                    print("Continue.....")
                    arrow()
                 #--------------------------Delete Sub Menu choice 2 by cons_name------------------------   
            elif d==2:
                print("Data in Your table is :")
                line()
                cur.execute('select *from consumer')
                rows=cur.fetchall()
                t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                for x,y,z,a in rows:
                    t.add_row([x,y,z,a])
                print(t)
                line()   
                c=input("Enter cons_name for delete record : ")
                cur.execute("select *from consumer where cons_name='%s' "%c)
                rows=cur.fetchall()
                print(rows)
                line()
                c=input("Enter cons_name: ")
                cur.execute(" delete from consumer where cons_name='%s' "%c)
                db.commit()
                arrow()
                print ("=====>  DATA REMOVED  <=====")
                #--------------------------Delete Sub Menu choice 3 by Address------------------------   
            elif d==3:
                print("Data in Your table is :")
                line()
                cur.execute('select *from consumer')
                rows=cur.fetchall()
                t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                for x,y,z,a in rows:
                    t.add_row([x,y,z,a])
                print(t)
                line()
                c=input("Enter address for delete record : ")
                cur.execute("select *from consumer where address='%s' "%c)
                rows=cur.fetchall()
                print(rows)
                line()
                c=input("Enter Address: ")               
                cur.execute(" delete from consumer where address='%s' "%c)
                db.commit()
                arrow()
                print ("=====>  DATA REMOVED  <=====")
                arrow()
            #--------------------------Delete Sub Menu choice 4 by s_id------------------------   
            elif d==4:
                print("Data in Your table is :")
                line()
                cur.execute('select *from consumer')
                rows=cur.fetchall()
                t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                for x,y,z,a in rows:
                    t.add_row([x,y,z,a])
                print(t)
                line()    
                c=input("Enter s_id for delete record : ")
                cur.execute(" select *from consumer where s_id='%s' "%c)
                rows=cur.fetchall()
                print(rows)
                line()
                c=input("Enter s_id: ")
                cur.execute("delete from consumer where s_id= '%s' "%c)
                db.commit()
                arrow()
                print ("=====>  DATA REMOED  <=====")
                arrow()
            elif d==5:
                break
            else:
                print ("Enter Valid Input.....Plese Continue")
                arrow()
     #-----------------------------Main Menu Choice 3 Update Record----------------------------------------
    elif m==3:
            while True:
                line()
                print(" **************Update Sub Menu ************** ")
                line()
                print("| 1=> Update All record                    |")
                print("| 2=> Update c_id only                     |")
                print("| 3=> Update cons_name  only               |")
                print("| 4=> Update address only                  |")
                print("| 5=> Update s_id only                     |")
                print("| 6=> Update c_id,cons_name                |")
                print("| 7=> Update c_id,cons_name,address        |")
                print("| 8=> Update c_id,cons_name, s_id          |")
                print("| 9=> Exit to Main Menu                    |")
                line()
                u=int(input('Enter your Choice (1 to 9) :'))
    #--------------------------Delete Sub Menu choice 1 all record------------------------
                if u==1:
                    print("Data in Your table is :")
                    line()
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                    line()
                    v1=input("Enter C_id: ")
                    v2=input("Enter Cons_name: ")
                    v3=input("Enter Address: ")
                    v4=input("Enter S_id: ")
                    cid=v1
                    cname=v2
                    addr=v3
                    sid=v4
                    sql='update consumer set c_id ="%s",cons_name="%s", address="%s" , s_id="%s" where c_id="%s"'%(cid,cname,addr,sid,cid)                       
                    cur.execute(sql)
                    db.commit()
                    arrow()
                    print ("=====>  DATA UPDATED  <=====")
                    arrow()
                    #--------------------------Update Sub Menu choice 2 c_id------------------------
                elif u==2:
                    print("Data in Your table is :")
                    line()
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                    line()
                    v1=input("Enter old C_id: ")
                    v2=input("Enter new C_id: ")                      
                    sql='update consumer set c_id ="%s" where c_id="%s"'%(v2,v1)                       
                    cur.execute(sql)
                    db.commit()
                    arrow()
                    print ("=====>  DATA UPDATED  <=====")
                    arrow()
            #--------------------------Update Sub Menu choice 3 Cons_Name------------------------
                elif u==3:
                    print("Data in Your table is :")
                    line()
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                    line()
                    v1=input("Enter old cons_name: ")
                    v2=input("Enter new cons_name: ")                      
                    sql='update consumer set cons_name ="%s" where cons_name="%s"'%(v2,v1)                       
                    cur.execute(sql)
                    db.commit()
                    arrow()
                    print ("=====>  DATA UPDATED  <=====")
                    arrow()
            #--------------------------Update Sub Menu choice 4 Address------------------------
                elif u==4:
                    print("Data in Your table is :")
                    line()
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                    line()
                    v1=input("Enter old Address: ")
                    v2=input("Enter new Address: ")                      
                    sql='update consumer set address ="%s" where address="%s"'%(v2,v1)                       
                    cur.execute(sql)
                    db.commit()
                    arrow()
                    print ("=====>  DATA UPDATED  <=====")
                    arrow()
            #--------------------------Update Sub Menu choice 5  s_id ------------------------
                elif u==5:
                    print("Data in Your table is :")
                    line()
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                    line()
                    v1=input("Enter old s_id: ")
                    v2=input("Enter new s_id: ")                      
                    sql='update consumer set s_id ="%s" where s_id="%s"'%(v2,v1)                       
                    cur.execute(sql)
                    db.commit()
                    arrow()
                    print ("=====>  DATA UPDATED  <=====")
                    arrow()
    #--------------------------Delete Sub Menu choice 6 c_id and cons_name  ------------------------
                elif u==6:
                    print("Data in Your table is :")
                    line()
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                    line()
                    v1=input("Enter C_id: ")
                    v2=input("Enter Cons_name: ")
                    cid=v1
                    cname=v2
                    sql='update consumer set c_id ="%s",cons_name="%s"where c_id="%s"'%(cid,cname,cid)                       
                    cur.execute(sql)
                    db.commit()
                    arrow()
                    print ("=====>  DATA UPDATED  <=====")
                    arrow()
#--------------------------Delete Sub Menu choice 7 c_id,cons_name,address------------------------
                elif u==7:
                    print("Data in Your table is :")
                    line()
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                    line()
                    v1=input("Enter C_id: ")
                    v2=input("Enter Cons_name: ")
                    v3=input("Enter Address: ")
                    cid=v1
                    cname=v2
                    addr=v3
                    sql='update consumer set c_id ="%s",cons_name="%s", address="%s" where c_id="%s"'%(cid,cname,addr,cid)                       
                    cur.execute(sql)
                    db.commit()
                    arrow()
                    print ("=====>  DATA UPDATED  <=====")
                    arrow()
    #--------------------------Delete Sub Menu choice 8 c_id,cons_name, s_id------------------------
                elif u==8:
                    print("Data in Your table is :")
                    line()
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','aadr','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                    line()
                    v1=input("Enter C_id: ")
                    v2=input("Enter Cons_name: ")
                    v4=input("Enter S_id: ")
                    cid=v1
                    cname=v2
                    addr=v3
                    sid=v4
                    sql='update consumer set c_id ="%s",cons_name="%s",  s_id="%s" where c_id="%s"'%(cid,cname,sid,cid)                       
                    cur.execute(sql)
                    db.commit()
                    arrow()
                    print ("=====>  DATA UPDATED  <=====")
                    arrow()
   #--------------------------Update Sub Menu choice 9 Exit ------------------------           
                elif u==9: break
                else:
                    arrow()
                    print ("Enter Valid Input.... Continue....")
                    arrow()
    #-----------------------------Main Menu Choice 4 Display Records----------------------------------------           
    elif m==4:
        while True:
                line()
                print(" **************Display Sub Menu**************")
                line()
                print("| 1=> Display All record                    |")
                print("| 2=> Display c_id only                     |")
                print("| 3=> Display cons_name  only               |")
                print("| 4=> Display address only                  |")
                print("| 5=> Display s_id only                     |")                
                print("| 6=> Display c_id,cons_name                |")
                print("| 7=> Display c_id,cons_name,address        |")
                print("| 8=> Display c_id,cons_name, s_id          |")
                print("| 9=> Exit to Main Menu                     |")
                line()
                dis=int(input('Enter your Choice (1 to 9)::'))
                #--------------------------Display Sub Menu choice 1 all record------------------------
                if dis==1:
                    cur.execute('select *from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','address','s_id'])
                    for x,y,z,a in rows:
                        t.add_row([x,y,z,a])
                    print(t)
                #--------------------------Display Sub Menu choice 2 c_id------------------------
                elif dis==2:
                    cur.execute('select c_id from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id'])
                    for x in rows:
                        t.add_row([x])
                    print(t)
                #--------------------------Display Sub Menu choice 3 cons_name------------------------
                elif dis==3:
                    cur.execute('select cons_name from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['cons_name'])
                    for x in rows:
                        t.add_row([x])
                    print(t)
                #--------------------------Display Sub Menu choice 4 Address------------------------
                elif dis==4:
                    cur.execute('select address from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['address'])
                    for x in rows:
                        t.add_row([x])
                    print(t)
                #--------------------------Display Sub Menu choice 5 s_id------------------------
                elif dis==5:
                    cur.execute('select s_id from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['s_id'])
                    for x in rows:
                        t.add_row([x])
                    print(t)                    
                #--------------------------Display Sub Menu choice 6 c_id,cons_name------------------------
                elif dis==6:
                    cur.execute('select c_id, cons_name from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name'])
                    for x,y in rows:
                        t.add_row([x,y])
                    print(t)                    
                #--------------------------Display Sub Menu choice 7 c_id,cons_name,aadress------------------------
                elif dis==7:
                    cur.execute('select c_id,cons_name,address from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','address'])
                    for x,y,z in rows:
                        t.add_row([x,y,z])
                    print(t)
                #--------------------------Display Sub Menu choice 8 c_id,cons_name,s_id------------------------
                elif dis==8:
                    cur.execute('select c_id,cons_name,s_id from consumer')
                    rows=cur.fetchall()
                    t = PrettyTable(['c_id','cons_name','s_id'])
                    for x,y,z in rows:
                        t.add_row([x,y,z])
                    print(t)
                #--------------------------Display Sub Menu choice 9 Exit------------------------
                elif dis==9:
                    break
                else:
                    arrow()
                    print ("Enter Valid Input.... Continue....")
                    arrow()
                #-----------------------------Main Menu Choice 5 Exit----------------------------------------        
    elif m==5:
        arrow()
        ch=input("y(for Continue)/n(Exit) :")
        if ch=='y' or ch=='Y':
            continue
        else:
            break
    else:
        arrow()
        print ("==>  Enter Valid Input  <==")
        arrow()
"""

"""
