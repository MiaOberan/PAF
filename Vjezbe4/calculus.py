import numpy as np
import math

def deriv(funkc,x,h):
    return(funkc(x+h)-funkc(x-h))/(2*h)

def deriv2(func,x,h):
    return (func(x+h) - func(x)) / h

def deriviraj(func,h,x1,x2,m=3):
    
    der_lista = []
    x_lista = np.arange(x1,x2,h)
    
    for x in x_lista:
        if m ==3:
            d = deriv2(func,x,h)
        elif m == 2:
            d = deriv(func,x,h)
        der_lista.append(d)
        
    return x_lista,der_lista

def integracija1(func,a,b,N):
    dx = (b-a)/N
    x_gornja = a
    x_donja = a+dx 
    gornja_m = 0
    donja_m = 0.
    for i in range(N):
        gornja_m += func(x_gornja)*dx
        donja_m += func(x_donja)*dx
        x_donja+= dx
        x_gornja += dx 
    return gornja_m,donja_m
def integracija(func,a,b,N):
    dx = (b-a)/N
    xk = a
    suma = 0
    for i in range(N):
        suma += (func(xk) + func(xk+dx))
        xk += dx
    integr = (dx/2)*suma
    return integr
