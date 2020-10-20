import random
print('Helo world')
n = int(input('Enter the Number of Names to be Entered : '))
p = int(input('Enter the number of Participants allowed in a group : '))

m = list()
o = list()
v = 0

f = open('output.txt', 'a')

for i in range(n):
    a = input('Enter the name : ')
    m.append(a)

random.shuffle(m)

while n // p != v:
    o.clear()
    w = random.choices(m, k=p)
    for y in w:
        if m.count(y) == 1:
            o.append(y)
            m.remove(y)
        else:
            break
    if len(o) == p:
        print(o)
        f.write(str(o))
        v += 1
