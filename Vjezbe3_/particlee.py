from math import sin,cos,radians
class Particle:
    def __innit(self,v0,theta,x0,y0):
        self.v0=v0
        self.theta=theta
        self.x0=x0
        self.y0=y0
        self.x_=[]
        self.y_=[]
    def printInfo(self):
        print(self.v0,self.theta,self.x0,self.y0)
    def reset(self):
        self.v0=None
        self.theta=None
        self.x0=None
        self.y0=None
    def __move(self,dt):
        g=9.81
        y=self.y0
        x=self.x0
        theta=radians(self.theta)
        vx=self.v0*cos(self.theta)
        x=self.x0+vx*dt
        vy=self.v0*sin(self.theta)
        vy=vy-g*dt
        y=self.yo*vy*dt
        self.x_.append(x)
        self.y_.append(y)
    def range(self,theta):
        g=9.81
        D=(v0**2)/g*sin*2*(radians(self.theta))
        print("Domet je",D,"metara")
    def plot_trajectory()