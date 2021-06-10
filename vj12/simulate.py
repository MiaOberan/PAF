import universe
import numpy as np
import matplotlib.pyplot as plt

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
mercury = universe.Planet("Mercury", 3.301e23, np.array((0.,0.387*au)), np.array((-47861.,0.)))
earth = universe.Planet("Earth", 5.9742e24, np.array((-1*au,0.)), np.array((0.,29783.)))
venus=universe.Planet("Venus", 4.869e24, np.array((-0.722*au,0.)),np.array((0.,-34965)))
mars=universe.Planet("Mars",6.4185e23, np.array((0.,-1.52*au)), np.array((23885, 0.)))
ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(earth)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(mars)
ss.evolve(2*year)

fig= plt.figure(figsize=(10,10))
plt.plot(sun.x,sun.y,label=sun.name,color="yellow", linewidth=5.0)
plt.plot(mercury.x,mercury.y,label=mercury.name,color="green")
plt.plot(mercury.x[-1],mercury.y[-1],"o",color="green")
plt.plot(earth.x,earth.y,label=earth.name,color="blue")
plt.plot(earth.x[-1],earth.y[-1],"o",color="blue")
plt.plot(venus.x,venus.y,label=venus.name,color="orange")
plt.plot(venus.x[-1],venus.y[-1],"o",color="orange")
plt.plot(mars.x,mars.y,label=mars.name,color="magenta")
plt.plot(mars.x[-1], mars.y[-1],"o",color="magenta")
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y graf')
plt.legend(loc="upper right")
plt.show()