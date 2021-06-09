import matplotlib.pyplot as plt
import math
F=float(input("Unesi silu: "))
m=float(input("Unesi masu: "))
t = []
x = []
v = []
a = []
dt = 0.01
vrijeme = 0
brzina = 0
pomak = 0
akceleracija = 0
for i in range(0,1000):
    vrijeme = vrijeme + dt
    t.append(vrijeme)
    akceleracija = F/m
    a.append(akceleracija)
    brzina = brzina + akceleracija*dt
    v.append(brzina)
    pomak = pomak + brzina*dt
    x.append(pomak)
plt.plot(t,x)
plt.show()
plt.plot(t,a)
plt.show()

    
    