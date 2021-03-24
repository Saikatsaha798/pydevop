import os,time

s=' '
while True:
    for i in range(100):
        p = '[' + i*s + 'e' + (99-i)*s + ']'
        print(p)
        time.sleep(0.05)
        os.system('cls')