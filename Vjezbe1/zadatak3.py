import matplotlib.pyplot as plt
x1=int(input("unesi x1:"))
y1=int(input("unesi y1:"))
x2=int(input("unesi x2:"))
y2=int(input("unesi y2:"))
k=(y2-y1)/(x2-x1)
print("y-{}={}*(x-{})".format(y1,k,x1))
x_kord=[x1,x2]
y_kord=[y1,y2]
plt.plot(x_kord,y_kord)
plt.show()