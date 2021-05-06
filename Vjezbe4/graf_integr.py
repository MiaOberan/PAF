import calculus
import matplotlib.pyplot as plt
import module
import math
import numpy as np

a = 0
b = 10
def f1(x):
    return x**2-4*x+2
def integr_f(x):
    return x**3/3-2*x**2+2*x

d_list = []
gornja = []
donja = []
trapezno = []
analiticko = []

dn = 50
for i in range(1,20):
    d = dn * i
    d_list.append(d)
   

for d in d_list:
    gm, dm = calculus.integriracija1(f1,a,b,d)
    trap = calculus.integracija(f1,a,b,d)
    analit = integr_f(b)-integr_f(a)
    gornja.append(gm)
    donja.append(dm)
    trapezno.append(trap)
    analiticko.append(analit)
    
plt.plot(d_list,gornja, '.')
plt.plot(d_list,donja, '.')
plt.plot(d_list,trapezno, '.')
plt.plot(d_list,analiticko, "m")

plt.show()
