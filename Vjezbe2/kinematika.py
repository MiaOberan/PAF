import matplotlib.pyplot as plt
from math import sin
from math import cos
def jednoliko_gibanje(F,m,t):
    a=F/m
    dt=1
    v=0
    x=0
    t=0
    akceleracija=[]
    brzina=[]
    pomak=[]
    vrijeme=[]
    for i in range(10):
        v=v+ a*dt
        x=x+v*dt
        t+=dt
        brzina.append(v)
        pomak.append(x)
        vrijeme.append(t)
        akceleracija.append(a)
    plt.subplot(311)
    plt.plot(vrijeme,pomak)
    plt.title("x-t graf")
    plt.subplot(312)
    plt.plolt(vrijeme,brzina,"r")
    plt.title("v-t graf")
    plt.subplot(313)
    plt.plot(vrijeme,akceleracija,"g")
    plt.title("a-t graf")
    plt.show()
def kosi_hitac(v0,theta,t):
    vx=v0*cos(theta)
    x=0
    y=0
    dt=1
    N=t*2
    t=0
    g=9.82
    t_lista=[]
    x_lista=[]
    y_lista=[]
    for i in range(N):
        x=vx*t
        y=v0*sin(theta)*t-(1/2)*g*t**2
        t+=dt
        x_lista.append(x)
        y_lista.append(y)
        t_lista.append(t)
    plt.subplot(311)
    plt.plot(x_lista,y_lista,"g")
    plt.subplot(312)
    plt.plot(t_lista,x_lista)
    plt.subplot(313)
    plt.plot(t_lista,y_lista,"r")
    plt.show()
