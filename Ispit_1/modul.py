import matplotlib.pyplot as plt

class Bullet:
    def __init__(self,y0,v0):
        self.y = y0
        self.v = v0
        self.t = 0
        self.x=0
        self.xlist=[]
        self.ylist = []
        self.vlist = []
        self.tlist = []
        self.xlist.append(self.x)
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)
        self.__print()
    def __print(self):
            print("Pocetna visina je: {} m\nPocetna brzina je: {} ms^-1".format(self.y,self.v))

    def change_y0(self,n):
        self.y = self.y+n

    def change_v0(self,m):
        self.v = self.v+m
    def restart(self):
        self.y = self.ylist[0]
        self.v = self.vlist[0]
        self.t = 0
        self.ylist = []
        self.vlist = []
        self.tlist = []
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)

    def euler(self,h0,dt):
        self.x=self.v0*dt
        self.v = self.v - 9.81 * dt
        self.y = self.y + self.v * dt
        self.t = self.t + dt
        self.xlist.append(self.x)
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)
        plt.plot(self.xlist,self.tlist)
        plt.xlabel('Domet')
        plt.ylabel('Visina')
        plt.show()


    def plot_trajectory(self):
        plt.plot(self.xlist,self.tlist)
        plt.xlabel('Domet')
        plt.ylabel('Visina')
        plt.show()

    def __move(self,dt):
        self.v = self.v - 9.81 * dt
        self.y = self.y + self.v * dt
        self.t = self.t + dt
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)

    def run_event(self,dt):
        while self.y > 0:
            self.__move(dt)
        return self.ylist, self.vlist, self.tlist
    def duration(self,dt):
        while self.y > 0:
            self.__move(dt)
        return self.t
    def __move_with_ar(self,dt,k):
        a = -9.81 - k * self.v
        self.v = self.v + a * dt
        self.y = self.y + self.v * dt
        self.t = self.t + dt
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)
    def run_event_with_ar(self,dt,k):
        while self.y > 0:
            self.__move_with_ar(dt,k)
        return self.ylist, self.vlist, self.tlist
    def duration_with_ar(self,dt,k):
        while self.y > 0:
            self.__move_with_ar(dt,k)
        return self.t

