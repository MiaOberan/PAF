import particlee as prt 
import matplotlib.pyplot as plt
p1 = prt.Particle(10,15,20,50,0.1)
print(p1.range(10))
p1.plot_trajectory()
p1.reset()
