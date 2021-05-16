import matplotlib.pyplot as plt
import math 

class projectile:
    def __init__(self):
        self.vx_list = []
        self.vy_list = []
        self.x_list = []
        self.y_list = []
        self.ax_list = []
        self.ay_list = []
        self.t_list = []

    def init(self,m,v0,theta,x0,y0,ro,cd,A,dt):
        self.m = m
        self.v0 = v0         
        self.theta = theta
        self.kut = self.theta*math.pi/180
        self.vx = self.v0*math.cos(self.kut)
        self.vy = self.v0*math.sin(self.kut)
        self.vx_list.append(self.vx)
        self.vy_list.append(self.vy)
        self.x = x0          
        self.y = y0
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        self.ro = ro         
        self.cd = cd
        self.A = A
        self.ax = 0
        self.ay = 0
        self.ax_list.append(self.ax)
        self.ay_list.append(self.ay)
        self.dt = dt
        self.t = 0
        self.t_list.append(self.t)
 
    def reset(self):
        self.m = 0
        self.v0 = 0        
        self.theta = 0
        self.vx = 0
        self.vy = 0
        self.vx_list = []
        self.vy_list = []
        self.x = 0
        self.y = 0
        self.x_list = []
        self.y_list = []
        self.ro = 0
        self.cd = 0
        self.A = 0
        self.ax = 0
        self.ay = 0
        self.ax_list = []
        self.ay_list = []
        self.dt = 0

    def __move(self):
        a = 9.81
        self.x += + self.vx*self.dt
        self.vy -= a*self.dt
        self.y += + self.vy*self.dt
        self.x_list.append(self.x)
        self.y_list.append(self.y)
    def move(self):
        while self.y >= 0:
            self.__move()
            self.t += self.dt
            self.t_list.append(self.t)

        return self.x_list, self.y_list

    def __ax(self,v):
        return -abs(self.vx*self.vx*self.ro*self.cd*self.A)/(2*self.m)

    def __ay(self,v):
        return -9.81-abs(self.vy*self.vy*self.ro*self.cd*self.A)/(2*self.m)
    
    def __move_ar(self):
        self.vx += self.ax*self.dt     
        self.x += self.vx*self.dt
        self.ax = self.__ax(self.vx)
        self.x_list.append(self.x)
        self.vx_list.append(self.vx)
        self.ax_list.append(self.ax)
        self.vy += self.ay*self.dt      
        self.y += self.vy*self.dt
        self.ay = self.__ay(self.vy)
        self.y_list.append(self.y)
        self.vy_list.append(self.vy)
        self.ay_list.append(self.ay)

    def move_ar(self):   
        while self.y >= 0:
            self.__move_ar()
            self.t += self.dt
            self.t_list.append(self.t)
        return self.x_list,self.y_list
        
    def plot_trajectory(self):
        plt.figure("Graf trenutno")
        plt.plot(self.x_list,self.y_list)
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.show()

    def range(self):
        self.move_ar() 
        return max(self.x_list)

    def analiticki_domet(self):
        D = ((self.v0**2)*math.sin(2*self.kut))/9.81
        return D