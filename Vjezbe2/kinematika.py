import matplotlib.pyplot as plt
from math import sin
from math import cos
from math import radians
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
    for i in range(N):
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
    plt.plot(vrijeme,brzina,"c")
    plt.title("v-t graf")
    plt.subplot(313)
    plt.plot(vrijeme,akceleracija,"m")
    plt.title("a-t graf")
    plt.show()
def kosi_hitac(v0,theta,t):
    theta2=radians(theta)
    vx=v0*cos(theta2)
    vy=v0*sin(theta2)
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
        x=x+vx*dt
        vy=vy-g*dt
        y=y+vy*dt
        t+=dt
        x_lista.append(x)
        y_lista.append(y)
        t_lista.append(t)
    plt.subplot(311)
    plt.plot(x_lista,y_lista,"k")
    plt.subplot(312)
    plt.plot(t_lista,x_lista)
    plt.subplot(313)
    plt.plot(t_lista,y_lista,"c",linewidth=2)
    plt.show()
