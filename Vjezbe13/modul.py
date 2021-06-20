import finalni as universe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random 

au = 1.496e11
day = 60*60*24
year = 365.242*day

min_mercury_distance=[]
min_venus_distance=[]
min_earth_distance=[]
min_mars_distance=[]
min_sun_distance=[]


sun = universe.Planet("Sun", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
earth = universe.Planet("Earth", 5.9742e24, np.array((-1*au,0.)), np.array((0.,29780.)))
mercury= universe.Planet("Mercury", 1.635e20, np.array((-0.3*au,0.)), np.array((0.,48000.)))
venus= universe.Planet("Venus", 1.635e18, np.array((-0.7*au,0.)), np.array((0.,35000.)))
mars= universe.Planet("Mars", 6.39e24, np.array((-1.524*au,0.)), np.array((0.,24100.)))
ss = universe.Universe() 

def signum():
    while True:
        broj=random.randint(-1,1)
        if broj !=0:
            return broj

for i in range(1000):

    rx, ry = signum()*random.randint(4*au,5*au), signum()*random.randint(4*au,5*au)
    vx, vy = -np.sign(rx)*random.randint(1*10**4,4*10**4), -np.sign(ry)*random.randint(1*10**4,4*10**4)
    r=np.array((rx,ry))
    v=np.array((vx,vy))
    m=random.randint(1*10**13,9.9*10**13)


    comet = universe.Planet("comet", m, r, v)    
    ss.add_planet(sun)
    ss.add_planet(earth)
    ss.add_planet(mercury)
    ss.add_planet(venus)
    ss.add_planet(mars)
    ss.add_planet(comet)
    

    ss.evolve(5.0*year)

    ss.delete_planet(comet)

    min_mercury_distance.append(min(mercury.dist)/au)
    min_venus_distance.append(min(venus.dist)/au)
    min_earth_distance.append(min(earth.dist)/au)
    min_mars_distance.append(min(mars.dist)/au)
    min_sun_distance.append(min(sun.dist)/au)
    ss.__init__()


fig, axs = plt.subplots(1, 5, sharey=True, tight_layout=True)
plt.xlim(0,1)
axs[0].hist(min_mercury_distance, len(min_mercury_distance), facecolor='magenta', alpha=0.5,label="Mercury")
axs[1].hist(min_venus_distance, len(min_venus_distance), facecolor='magenta', alpha=0.5,label="Venus")
axs[2].hist(min_earth_distance, len(min_earth_distance), facecolor='magenta', alpha=0.5,label="Earth")
axs[3].hist(min_mars_distance, len(min_mars_distance), facecolor='magenta', alpha=0.5,label="Mars")
axs[4].hist(min_sun_dist, len(min_sun_dist), facecolor='magenta', alpha=0.5,label="Sun")
plt.show()
plt.savefig("Histogram kometa")

#treci zadatak

ss.add_planet(sun)
ss.add_planet(earth)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(mars)
ss.add_planet(comet)
    

ss.evolve(5.0*year)

fig, ax= plt.figure(figsize=(10,10)), plt.axes(xlim=(-5*au, 5*au), ylim=(-5*au, 5*au))

mercury_list, = ax.plot([], [], 'o',color="orange")
venus_list, = ax.plot([], [], 'o',color="cyan")
earth_list, = ax.plot([], [], 'o',color="blue")
mars_list, = ax.plot([], [], 'o',color="red")
sun_list, = ax.plot([], [], 'o',color="yellow")
comet_list, =ax.plot([], [], 'o', color="magenta")

plt.plot(sun.x,sun.y,label=sun.name,color="yellow", linewidth=2.0)
plt.plot(earth.x,earth.y,label=earth.name,color="blue")
plt.plot(mercury.x,mercury.y,label=mercury.name,color="orange")
plt.plot(venus.x,venus.y,label=venus.name,color="cyan")
plt.plot(mars.x,mars.y,label=mars.name,color="red")
plt.plot(comet.x,comet.y,label=comet.name,color="magenta")
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y graf')
plt.legend(loc="upper right")

x_mercury, x_venus, x_earth, x_mars, x_sun, x_comet = [], [], [], [], [], []
y_mercury, y_venus, y_earth, y_mars, y_sun, y_comet = [], [], [], [], [], []


def planets():

    mercury_list.set_data([], [])
    venus_list.set_data([], [])
    earth_list.set_data([], [])
    mars_list.set_data([], [])
    sun_list.set_data([], [])
    comet_list.set_data([], [])

    return mercury_list, venus_list, earth_list, mars_list, sun_list,

def animation(i):

    x_sun.append(sun.x[i])
    y_sun.append(sun.y[i])

    x_mercury.append(mercury.x[i])
    y_mercury.append(mercury.y[i])
    
    x_venus.append((venus.x[i]))
    y_venus.append((venus.y[i]))

    x_earth.append((earth.x[i]))
    y_earth.append((earth.y[i]))

    x_mars.append((mars.x[i]))
    y_mars.append((mars.y[i]))
    
    x_comet.append(comet.x[i])
    y_comet.append(comet.y[i])

    mercury_list.set_data(x_mercury[i], y_mercury[i])
    venus_list.set_data(x_venus[i], y_venus[i])
    earth_list.set_data(x_earth[i], y_earth[i])
    mars_list.set_data(x_mars[i], y_mars[i])
    sun_list.set_data(x_sun[i], y_sun[i])
    comet_list.set_data(x_comet[i],y_comet[i])

    return mercury_list,

animation = FuncAnimation(fig, animation, init_func=planets, interval=2)
plt.show()
