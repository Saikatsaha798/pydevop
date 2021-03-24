import mysql.connector,time

con = mysql.connector.connect(host='localhost', user='root', password='0000', database='database1')
print('Connection is established successfully....')
c = con.cursor()
time.sleep(2)
a = ['select * from emp;', 'delete from emp where ename=\'JAMES\';']

c.execute(a[0])
l = c.fetchall()
print('Values are : ')
for i in l:
    print(i)
time.sleep(2)
c.execute(a[1])
con.commit()
con.close()
print('The Column Deleted.')