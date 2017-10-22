from sympy import *
from math import e
x=Symbol("x")
a=Symbol("a")
p=Symbol("p")
print(diff(a*e**x+2*x**p+3*ln(x), x))
