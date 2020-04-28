from typing import List

import sympy as sp
from mendeleev import *

sp.init_printing()

o = input('Enter the Symbol of element : ')
o = element(o)
z = o.atomic_number

r = 0
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

k = list()

for n in range(1, 8):
    for j in range(n):
        a = n + j
        sb = list(c[j].keys())
        g = c[j][sb[0]]
        k.append([a, sb[0], n, g])

while e > 0:
    for j in range(n):
        if e == 0:
            break
        elif len(k) == 0:
            break
        elif e < k[0][3]:
            if len(k) == 1:
                u = sp.symbols(k[0][1])
                v = k[0][2] * u ** e
                econ.append(v)
                k.pop(0)
            elif k[0][0] < k[1][0]:
                u = sp.symbols(k[0][1])
                v = k[0][2] * u ** e
                econ.append(v)
                k.pop(0)
            elif k[0][0] > k[1][0]:
                u = sp.symbols(k[1][1])
                v = k[1][2] * u ** e
                econ.append(v)
                k.pop(1)
            else:
                if k[0][2] < k[1][2]:
                    u = sp.symbols(k[0][1])
                    v = k[0][2] * u ** e
                    econ.append(v)
                    k.pop(0)
                else:
                    u = sp.symbols(k[1][1])
                    v = k[1][2] * u ** e
                    econ.append(v)
                    k.pop(1)
            e = 0
            break
        elif len(k) == 1:
            u = sp.symbols(k[0][1])
            r = k[0][3]
            v = k[0][2] * u ** k[0][3]
            econ.append(v)
            k.pop(0)
            e = 0
            break
        elif k[0][0] < k[1][0]:
            r = k[0][3]
            u = sp.symbols(k[0][1])
            v = k[0][2] * u ** k[0][3]
            econ.append(v)
            e -= k[0][3]
            k.pop(0)
        elif k[0][0] > k[1][0]:
            r = k[1][3]
            u = sp.symbols(k[1][1])
            v = k[1][2] * u ** k[1][3]
            econ.append(v)
            e -= k[1][3]
            k.pop(1)
        else:
            if k[0][2] < k[1][2]:
                r = k[0][3]
                u = sp.symbols(k[0][1])
                v = k[0][2] * u ** k[0][3]
                econ.append(v)
                e -= k[0][3]
                k.pop(0)
            else:
                r = k[1][3]
                u = sp.symbols(k[1][1])
                v = k[1][2] * u ** k[1][3]
                econ.append(v)
                e -= k[1][3]
                k.pop(1)
    n += 1

if z == 24 or 29:
    s = sp.symbols('s')
    p = sp.symbols('p')
    d = sp.symbols('d')
    if z == 24:
        econ = [s ** 2, 2 * s ** 2, 2 * p ** 6, 3 * s ** 2, 3 * p ** 6, 4 * s ** 1, 3 * d ** 5]
    if z == 29:
        econ = [s ** 2, 2 * s ** 2, 2 * p ** 6, 3 * s ** 2, 3 * p ** 6, 4 * s ** 1, 3 * d ** 10]

print('Electronic Configuration of', z, ',', o.name, 'is : ', econ)
