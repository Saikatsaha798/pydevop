def pushstack(l,a):
    l.append(a)
    print(f'\'{a}\' was pushed in stack.')

def popstack(l):
    print(f'\'{l.pop()}\' was deleted.')

def displaystack(l):
    for i in l[::-1]:
        print(i)

if __name__ == '__main__':
    l=[]
    while True:
        print('***MENU***'
        '\n1. Push in Stack'
        '\n2. Pop out from Stack'
        '\n3. Display the Stack'
        '\n4. Exit')
        ch = int(input('Enter the Choice : '))
        if ch==1:
            a = input('Enter the Emp Id : ')
            b = input('Enter the Emp Name : ')
            c = (a,b)
            pushstack(l,c)
        elif ch==2:
            if len(l)!=0:
                popstack(l)
            else:
                print('Error: UnderFlow')
        elif ch==3:
            if len(l)!=0:
                displaystack(l)
            else:
                print('Error: UnderFlow')
        elif ch==4:
            print('Exiting the Program ...')
            break
        else:
            print('Error: Wrong Choice')