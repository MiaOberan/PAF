from math import sin, cos, radians
import matplotlib.pyplot as plt
v0 = 20
theta = radians(45)
v_x = v0 * cos(theta)
x = 0
y = 0
dt = 0.5
t = 0
g = 9.81
vy = v0*sin(theta)
t_l = []
x_l = []
y_l = []

for i in range(20):
    x = x + v_x * dt
    vy = vy - g*dt
    y = y + vy*dt
    t += dt

    x_l.append(x)
    y_l.append(y)
    t_l.append(t)

plt.subplot(311)
plt.plot(x_l,y_l, 'g')
plt.title('y-x graf')

plt.subplot(312)
plt.plot(t_l,x_l)
plt.title('x-t graf')
plt.subplot(313)
plt.plot(t_l,y_l, 'r')
plt.title('y-t graf')
plt.show()
