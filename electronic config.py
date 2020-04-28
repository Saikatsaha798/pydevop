import sympy as sp
from mendeleev import *

sp.init_printing()

o = input('Enter the Symbol of element : ')
o = element(o)
z = o.atomic_number

e = z
n = 1
econ = list()

c = {0: {'s': 2},
     1: {'p': 6},
     2: {'d': 10},
     3: {'f': 14},
     4: {'g': 18},
     5: {'h': 22},
     6: {'i': 26}}

while e != 0:
    for l in range(n):
        u = list(c[l].keys())
        if e > c[l][u[0]]:
            sb = sp.symbols(u[0])
            expr = n * sb ** c[l][u[0]]
            econ.append(expr)
            e -= c[l][u[0]]
        elif e < c[l][u[0]]:
            sb = sp.symbols(u[0])
            expr = n * sb ** e
            econ.append(expr)
            e = 0
            break
        else:
            break
    n += 1

print('Electronic Configuration of', z, ',', o.name, 'is : ', econ)
