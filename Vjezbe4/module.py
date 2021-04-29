import calculus as ca
def f1(x):
    return 5*x**2-3*x
def if1(x):
    return 5*x**3/3 - 3*x**2/2
a,b=ca.integracija1(f1,0.0,1.0,1000)
print(a,b)
print(if1(1)-if1(0))
