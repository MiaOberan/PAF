from math import sin,cos,radians,sqrt
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,v0,theta,x0,y0,dt):
        self.v0=v0
        self.theta=radians(theta)
        self.x=x0
        self.y=y0
        self.x_=[]
        self.y_=[]
        self.vy_ = []
        self.x_.append(x0)
        self.y_.append(y0)
        self.vx = v0*cos(self.theta)
        self.vy = v0*sin(self.theta)
    def printInfo(self):
        print(self.v0,self.theta,self.x0,self.y0)
    def reset(self):
        self.v0=0
        self.theta=0
        self.x0=0
        self.y0=0
        self.y_ = []
        self.x_ = []
        self.vy_ = []
    def __move(self,dt):
        g=9.81
        theta=radians(self.theta)
        self.x = self.x + self.vx*dt
        self.vy = self.vy - g*dt
        self.y = self.y + self.vy*dt
        self.x_.append(self.x)
        self.y_.append(self.y)
        self.vy_.append(self.vy)
    def range(self,dt):
        while True: 
            self.__move(dt)
            if self.y <= 0:
                break
        return self.x
    def plot_trajectory(self):
       
        plt.plot(self.x_,self.y_)
        plt.xlabel('Domet')
        plt.ylabel('Visina')
        plt.show()
        
    def analiticko_rjesenje(self,theta):
        g=9.81
        D = (self.v0**2/g) * math.sin(2 * self.theta)
        return D
p1 = Particle(70,15,0,0,0.01)
print(p1.range(0.001))
p1.plot_trajectory()
p1.reset()
