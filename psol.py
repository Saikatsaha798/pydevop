op = ['*','-','+','/']
l = []
CH = 'Y'
while CH == 'Y' or CH == 'y':
    inp=input('Enter : ')
    try:
        a = int(inp)
        l.append(a)
        act='PUSH'
    except:
        if inp in op:
            if l == [] or len(l) == 1:
                pass
            else:
                a = l[-2]
                b = l[-1]
                exp = f'{a}{inp}{b}'
                c = eval(exp)
                l.remove(a)
                l.remove(b)
                l.append(c)
                act='POP 2 ELEMENTS'
    if l==[]:
        list='EMPTY'
    else:
        list=l
    if act == 'PUSH':
        print(f'Symbol\tAction\tStatus\tOutput')
        print(f'{inp}\t{act}\t{list}')
    if act=='POP 2 ELEMENTS':
        print(f'Symbol\tAction\t\tStatus\tOutput')
        print(f'{inp}\t{act}\t{list}\t{exp}={c}')
    CH = input('Want to do More ?')
