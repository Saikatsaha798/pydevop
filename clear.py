import os,time,random,string

p=''
while True:
    for i in range(8):
        p+=random.choice(string.ascii_letters)
    print(p)
    time.sleep(0.3)
    p=''
    os.system('cls')
        
