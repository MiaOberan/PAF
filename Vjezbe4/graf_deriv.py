import calculus
import matplotlib.pyplot as plt
import module
import math
import numpy as np

def f4(x):
    return 5*x**3 - 2*x**2+2*x-3
xk1 = -2
xk2 = 2
h = 0.1
x_l1 = np.arange(xk1,xk2,h)
d_l1 = []
for x in x_l1:
    d =15*x**2 - 4*x +2
    d_l1.append(d)

a,b = calculus.deriviraj(f4,0.1,-2,2)
plt.plot(x_l1,d_l1)
plt.scatter(a,b, s = 5, color = 'm')
plt.show()

print(calculus.deriv2(f4,1,0.1))
x=1
d =15*x**2 - 4*x +2
print(d)

def ftrigon(x):
    return math.sin(2*x) - math.cos(x)
xt1 = -10
xt2 = 10
ht = 0.01
d_l2 = []
x_l2 = np.arange(xt1,xt2,ht)

for x in x_l2:
    d = math.cos(2*x)*2+math.sin(x)
    d_l2.append(d)

c,d = calculus.deriviraj(ftrigon,0.01,-10,10)
plt.plot(x_l2,d_l2)
plt.scatter(c,d, s = 1, color = 'k')
plt.show()
