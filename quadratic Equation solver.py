def equation(a,b,c):
    q=lambda x: a*x**2+b*x+c
    return q
def main():
    r=list()
    a=int(input("Enter the coefficient of x^2 : "))
    b=int(input("Enter the coefficient of x : "))
    c=int(input("Enter the constant term : "))
    e=equation(a,b,c)
    d=b**2-4*a*c
    if d>=0:
        for i in range(-1000,1000):
            if e(i)==0:
                r.append(i)
                print("Root of Equation : ", r)
    else:
        print("No real root exist !!!!!")

main()