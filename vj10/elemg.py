import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
class elemg:
    def __init__(self,q,m,v,B,E,r,dt):
        self.q = q
        self.m= m
        self.v = v
        self.B = B
        self.E = E 
        self.r = r 
        self.dt = dt
        self.x_ = []
        self.y_ = []
        self.z_ = []
        self.x_.append(self.r[0])
        self.y_.append(self.r[1])
        self.z_.append(self.r[2])
        self.t = 0
       
    def reset(self):
        del self.q 
        del self.m
        del self.v 
        del self.B 
        del self.E  
        del self.r 
        del self.x_ 
        del self.y_ 
        del self.z_ 
        del self.x_
        del self.y_
        del self.z_
    
    def akcel(self,v):
        a = (self.q/self.m)*(self.E+np.cross(v,self.B))
        return a 
    def __move_Euler(self):
        a = self.akcel(self.v)
        self.v = self.v + a*self.dt
        self.r = self.r + self.v*self.dt
        self.t += self.dt
        self.x_.append(self.r[0])
        self.y_.append(self.r[1])
        self.z_.append(self.r[2])

    def Euler(self,t):
        while self.t<= t:
           self. __move_Euler()
        return self.x_,self.y_,self.z_
    
    def __move_RK(self):
        k1v = self.akcel(self.v)*self.dt
        k1r = self.v*self.dt
        k2v = self.akcel(self.v + k1v*0.5)*self.dt
        k2r = (self.v + k1v*0.5)*self.dt
        k3v = self.akcel(self.v + k2v*0.5)*self.dt   
        k3r = (self.v + k2v*0.5)*self.dt
        k4v = self.akcel(self.v + k3v*0.5)*self.dt   
        k4r = (self.v + k3v*0.5)*self.dt

        self.v = self.v + (k1v+2*k2v+2*k3v+k4v)/6
        self.r = self.r + (k1r+2*k2r+2*k3r+k4r)/6
        self.a = self.akcel(self.v)
        self.t += self.dt
        self.x_.append(self.r[0])
        self.y_.append(self.r[1])
        self.z_.append(self.r[2])

    
    def RK(self,t):
        while self.t<= t:
           self. __move_RK()
        return self.x_,self.y_,self.z_

    def plot_trajectory(self):
        ax = plt.axes(projection='3d')
        ax.plot3D(self.x_,self.y_,self.z_)
        plt.show()