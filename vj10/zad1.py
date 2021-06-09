import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import elemg as em 

p = em.elemg(1,1,np.array((0.1,0.1,0.1)),np.array((0,0,1)),np.array((0,0,0)),np.array((0,0,0)),0.01)
p.Euler(20)

e = em.elemg(-1,1,np.array((0.1,0.1,0.1)),np.array((0,0,1)),np.array((0,0,0)),np.array((0,0,0)),0.01)
e.Euler(20)

ax = plt.axes(projection='3d')
ax.plot3D(e.x_,e.y_,e.z_,"k")
ax.plot3D(p.x_,p.y_,p.z_,"m")
plt.show()