import tkinter as tk


def list_avg(lst):
    L = len(lst)
    sum = 0
    for i in lst:
        sum += i
    return sum / L


def main():
    print("Number of Data")
    a = int(input())
    l = []
    for i in range(a):
        b = int(input("Enter the Number : "))
        l.append(b)
    avg = list_avg(l)
    print("Average is= ", avg)


if __name__ == '__main__':
    main()
