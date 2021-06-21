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

    def plot_trajectory(self,dt,t):
        x,v,a,t = self.oscillate(dt,t)
        plt.subplot(1,3,1)
        plt.plot(t,x)
        plt.subplot(1,3,2)
        plt.plot(t,v)
        plt.subplot(1,3,3)
        plt.plot(t,a)
        plt.show()
    
    def reset(self):
        del self.k
        del self.m
        del self.x
        del self.v
        del self.a
        del self.t
        del self.x_l
        del self.v_l
        del self.a_l
        del self.t_l
    
    def preciznost(self,dt,t=2):
        self.oscillate(dt,t)
        plt.scatter(self.t_l,self.x_l)
        plt.title('x-t graf')
        
    def analiticki(self,dt,t1=2):
        self.x_l=[]
        self.t_l=[]
        self.omega=math.sqrt(self.k/self.m)
        self.t=0
        while self.t<=t1:
            x=self.x*math.cos(self.omega*self.t)
            self.t+=dt
            self.x_l.append(x)
            self.t_l.append(self.t)
        return self.x_l,self.t_l
    def period(self,dt,t):
        A = self.x
        T = 0
        self.oscillate(dt,t)
        for x in self.x_l:
                if x > 0:
                    T += dt
                else:
                    break
        print(4*T)

    def T_analiticki(self):
        T = 2*math.pi*math.sqrt(self.m/self.k)
        print(T)
            
        

        
           
            
        

        
        
    
#h1 = HarmonicOscillator(10,0.1,0.3,0)
#h1.period(0.01,5)

#h1.plot_trajectory(0.01,5)
#plt.show()
