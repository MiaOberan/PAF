import projectile as ptl 
import matplotlib.pyplot as plt

p = ptl.Projectile()

p.init(10,10,60,0,0,1.2,0.1,0.5,0.01)
x1,y1 = p.move_ar()
p.reset()
p.init(10,10,60,0,0,1.2,0.1,0.5,0.01)
x2,y2 = p.runge_kutta()   


plt.plot(x1,y1, label = "Euler")
plt.plot(x2,y2, c = "magenta", label = "Runge-Kutta")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("x-y graf")
plt.legend(loc = "upper right")
plt.show()