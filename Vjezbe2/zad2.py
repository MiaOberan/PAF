from math import sin
from math import cos
from math import pi
import matplotlib.pyplot as plt
v0=50
theta=30
theta=(theta/360)*2*pi
vx=v0*cos(theta)
vy=v0*sin(theta)
x=0
y=0
dt=0.1
t=0
g=9.82
t_lista=[]
x_lista=[]
y_lista=[]
for i in range(100):
    x=x+vx*dt
    vy=vy-g*dt
    y=y+vy*dt
    t+=dt
    x_lista.append(x)
    y_lista.append(y)
    t_lista.append(t)
plt.subplot(311)
plt.plot(x_lista,y_lista,"m")
plt.title("y-x graf")
plt.subplot(312)
plt.plot(t_lista,x_lista,"k")
plt.title("x-t graf")
plt.subplot(313)
plt.plot(t_lista,y_lista,"c")
plt.title("y-t graf")
plt.show()    
