import matplotlib.pyplot as plt
import modul
import math
import calculus
def f1(x):
    return x*x-2*x

def f2(x):
    return math.sin(x)
def f3(x):
    return x**2
def f4(x):
    return 5*x**3 - 2*x**2+2*x-3

print(modul.value(f1,1))
print(modul.value(f2,1))
print(calculus.deriviraj3(f3,0.01,2))
print(calculus.deriviraj2(f3,0.01,2))
