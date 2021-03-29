from math import sin,cos,radians
class Particle:
    def __innit(self,v0,theta,x0,y0,dt):
        self.v0=v0
        self.theta=theta
        self.x0=x0
        self.y0=y0
        self.x_=[]
        self.y_=[]
        self.dt=dt
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
        while True: 
            self.__move()
            if self.y0 <= 0:
                break
    def plot_trajectory(self):
        x_kord = [self.x]
        y_kord = [self.y]
        plt.scatter(x_cord,y_cord,s=1)
        plt.xlabel('Domet')
        plt.ylabel('Visina')
        plt.show()
        
     def analiticko_rjesenje(self,theta):
        g=9.81
        D = (self.v0**2/g) * math.sin(2 * self.theta)
        return D
