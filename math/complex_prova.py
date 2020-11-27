import cmath
from math import sqrt
from numpy import around
I = 1j
a = 1
b = sqrt(2) / 2 + I * sqrt(2) / 2
a += around(cmath.exp(I * cmath.pi / 4), decimals=10)
print(around(a * b, decimals=5))