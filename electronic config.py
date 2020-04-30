# Importing modules that are required.
import sympy as sp  # Required for dictating the sub-shells with number of electrons.
from mendeleev import *  # Required for synthesis of data from Periodic Table.

sp.init_printing()

# Taking the value from the user.
o = input('Enter the Symbol of element : ')

# Synthesising the Atomic Number from the symbol.
o = element(o)
z = o.atomic_number

# Declaring the Variables and Lists.
r = 0
e = z
n = 1
econ = list()
k = list()

# Creating a Nested Dictionary of Sub-shells.
c = {0: {'s': 2},
     1: {'p': 6},
     2: {'d': 10},
     3: {'f': 14},
     4: {'g': 18},
     5: {'h': 22},
     6: {'i': 26}}

# Inserting Frame Model for the Electrons Number to be entered later.
for n in range(1, 8):
    for j in range(n):
        a = n + j
        sb = list(c[j].keys())
        g = c[j][sb[0]]
        k.append([a, n, sb[0], g])

# Sorting the list.
k.sort()

# Basic Calculation and Entering the data in the frame and making ready to be displayed.
for n in range(1, 8):
    for j in range(n):
        if e == 0:
            break
        elif len(k) == 0:
            break
        elif e < k[0][3]:
            u = sp.symbols(k[0][2])
            v = k[0][1] * u ** e
            econ.append(v)
            k.pop(0)
            e = 0
            break
        elif len(k) == 1:
            u = sp.symbols(k[0][2])
            r = k[0][3]
            v = k[0][1] * u ** k[0][3]
            econ.append(v)
            k.pop(0)
            e = 0
            break
        else:
            r = k[0][3]
            u = sp.symbols(k[0][2])
            v = k[0][1] * u ** k[0][3]
            econ.append(v)
            e -= k[0][3]
            k.pop(0)

# Declaring Output for the Exceptions.
s = sp.symbols('s')
p = sp.symbols('p')
d = sp.symbols('d')
if z == 24:
    econ = [s ** 2, 2 * s ** 2, 2 * p ** 6, 3 * s ** 2, 3 * p ** 6, 4 * s ** 1, 3 * d ** 5]
if z == 29:
    econ = [s ** 2, 2 * s ** 2, 2 * p ** 6, 3 * s ** 2, 3 * p ** 6, 4 * s ** 1, 3 * d ** 10]

# Printing the Output.
print('Electronic Configuration of', z, ',', o.name, 'is : ', econ)
