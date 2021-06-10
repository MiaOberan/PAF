import math
import matplotlib.pyplot as plt
class HarmonicOscillator:
    def __init__(self,k,m,x0,v0):
        self.x_l = []
        self.v_l = []
        self.a_l = []
        self.t_l = []
        self.k = k
        self.m = m
        self.x = x0
        self.v = v0
        self.a = -(self.k*self.x)/self.m
        self.t = 0
        self.x_l.append(self.x)
        self.v_l.append(self.v)
        self.a_l.append(self.a)
        self.t_l.append(self.t)

    def oscillate(self,dt,t):
        N = int(t/dt)
        for i in range(N):
            self.a = -(self.k*self.x)/self.m
            self.v = self.v + self.a*dt
            self.x = self.x + self.v*dt
            self.t += dt
            self.x_l.append(self.x)
            self.v_l.append(self.v)
            self.a_l.append(self.a)
            self.t_l.append(self.t)
        return self.x_l,self.v_l,self.a_l,self.t_l
   