from math import sin,cos,radians, sqrt
import matplotlib.pyplot as plt
class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.v0 = v0
        self.theta = radians(theta)
        self.x = x0
        self.y = y0
        self.x_ = []
        self.y_ = []
        self.x_.append(x0)
        self.y_.append(y0)
        self.vx = v0*cos(self.theta)
        self.vy = v0*sin(self.theta)
        self.t = 0
        self.vy_ = []
    
        
    def printInfo(self):
        print(f'{self.v0},{self.theta},{self.x},{self.y}')
    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.x0 =0
        self.y0 = 0
        self.y_ = []
        self.x_ = []
        self.vy_ = []
    
        
    def __move(self, dt):
        g = 9.81
        self.x = self.x + self.vx*dt
        self.vy = self.vy - g*dt
        self.y = self.y + self.vy*dt
        self.x_.append(self.x)
        self.y_.append(self.y)
        self.vy_.append(self.vy)
    def range(self,dt):
        x = self.x
        while True:
            self.__move(dt)
            if self.y <= 0:
                break
        
        return self.x-x
    
    def plot_trajectory(self):
        plt.plot(self.x_,self.y_)
        plt.show()
    
    def analiticki(self):
        D = (self.v0**2*sin(2*self.theta))/9.81
        return D
p1 = Particle(70,15,0,0,0.01)
print(p1.range(0.001))
p1.plot_trajectory()
p1.reset()

