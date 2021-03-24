import numpy as np

def add():
    m = list()
    nr = int(input('Enter the amount of row : '))
    nc = int(input('Enter the amount of column : '))
    if nr == 0 or nc == 0:
        print('Wrong Number entered !!!')
    else:
        for i in range(1, nr+1):
            r = list()
            for j in range(1, nc+1):
                e = int(input(f'Enter the element with matrix [{i},{j}]'))
                r.append(e)
            m.append(r)
        return m

def transpose(m):
    mt = list()
    for i in range(len(m[0])):
        li = list()
        for j in m:
            li.append(j[i])
        mt.append(li)
    return mt


def show(m):
    print(np.array(m))

def continuer():
    cc = input('Want to do more ? [y/n]')
    if cc != 'y' and cc != 'Y':
        exit()
        print(f'{len(lm)} matrix was created.')

if __name__ == "__main__":
    lm = list()
    while True:
        print('What you want to do ?' 
        '\n1. Add Matrix'
        '\n2. Show Matrix'
        '\n3. Transpose Matrix')
        c = int(input('Enter your choice : '))
        if c == 1:
            m = add()
            lm.append(m)
            continuer()

        
        elif c == 2:
            for i in lm:
                show(i)
            continuer()

        
        elif c == 3:
            for i in lm:
                mt = transpose(i)
                show(mt)
            continuer()