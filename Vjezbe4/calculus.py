import module
import numpy as np
import math

def f1(x):
    return 5*x**3-2*x**2+2*x-3
print(module.deriv(f1,1,0.0001))
def deriv(funkc,x,h):
    return(funkc(x+h)-funkc(x-h))/(2*h)

def deriv2(funkc,h,x1,x2):
    deriv_lista=[]
    x_list=np.arange(x1,x2,h)
    for x in x_list:
        der=deriv(funkc,x,h)
        deriv_lista.append(der)
    return x_list,deriv_lista

x,y=deriv2(f1,0.1,1,3)
a,b=deriv2(f1,0.001,1,2)
print(a,b)
