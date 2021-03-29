import particlee as prt 
import matplotlib.pyplot as plt

p1 = prt.Particle(0,0,10,60,0.01)
dt_ = []
dt = 0.00
greske = []

for i in range(100):
    dt = dt + 0.01
    p1.init(0, 0, 10, 60,dt)
    greska = abs(p1.range() - p1.analiticko_rjesenje())/p1.analiticko_rjesenje()*100
    dt_.append(dt)
    greske.append(greska)
    p1.reset()

plt.xlabel('dt/s')
plt.ylabel('greska/ % ')
plt.plot(dt_, greske,"m")
plt.show()
