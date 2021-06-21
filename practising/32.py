import math
import matplotlib.pyplot as plt
import particleV3 as prt 
dt_l = []
pogreska = []
p = prt.Particle(10,60,0,0)
dt = 0
for i in range(100):
    
    p = prt.Particle(10,60,0,0)
    dt += 0.001
    gr = math.fabs(((p.range(dt)-p.analiticki())/p.analiticki())*100)
    dt_l.append(dt)
    pogreska.append(gr)
    p.reset()
plt.plot(dt_l,pogreska)
plt.show()
