import math
import matplotlib.pyplot as plt
class VertikalniHitac:
    def __init__(self,h0,v0):
        self.h0 = h0
        self.v0 = v0
    def objekt(self):
        print("uspjesno stvoren objekt,pocetna brzina je ",self.v0,"m/s a visina je",self.h0,"m")
    def reset_brzina(self):
        self.v0=0
    def reset_visina(self):
        self.h0=0
    def deriv(funkc,v0,h0):
        return(funkc(v0+h0)-funkc(v0-h0))/(2*h0)
        
    def vert_hitac(v0,theta,h0,t):
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
        for i in range(100):
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
        plt.plot(t_lista,x_lista,"m")
        plt.subplot(313)
        plt.plot(t_lista,y_lista,"c",linewidth=2)
        plt.show()






