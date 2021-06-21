import calculus
import matplotlib.pyplot as plt
import modul
import math
import numpy as np
def f4(x):
    return 5*x**3 - 2*x**2+2*x-3
xk1 = -2
xk2 = 2
hk = 0.1
x_l1 = np.arange(xk1,xk2,hk)
d_l1 = []
for x in x_l1:
    d = 15*x**2 - 4*x +2
    d_l1.append(d)

a,b = calculus.derivacija(f4,0.1,-2,2)
plt.plot(x_l1,d_l1)
plt.scatter(a,b, s = 5, color = 'r')
plt.show()

def ftrig(x):
    return math.sin(2*x) - math.cos(x)
xt1 = -10
xt2 = 10
ht = 0.01
d_l2 = []
x_l2 = np.arange(xt1,xt2,ht)

for x in x_l2:
    d = math.cos(2*x)*2+math.sin(x)
    d_l2.append(d)

c,d = calculus.derivacija(ftrig,0.01,-10,10)
plt.plot(x_l2,d_l2)
plt.scatter(c,d, s = 1, color = 'r')
plt.show()
