import projectile as ptl 
import matplotlib.pyplot as plt

p = ptl.projectile()

p.init(20,10,70,0,0,1.2,1,0.5,0.01)
x1,y1 = p.move()
p.reset()
p.init(20,10,70,0,0,1.2,0.1,0.5,0.01)
x2,y2 = p.move_ar()

plt.plot(x1,y1, label = "bez otpora zraka")
plt.plot(x2,y2, c = "red", label = "s otporom zraka")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Eulerova metoda")
plt.legend()
plt.show()