def average(sum,n):
                a=sum/n
                return a
def main():
                c=0
                n=int(input("Enter the number of data to be entered "))
                for i in range(1,n+1):
                                b=float(input("Enter the data "))
                                c+=b
                av=average(c,n)
                print("Average calculated is",av)
