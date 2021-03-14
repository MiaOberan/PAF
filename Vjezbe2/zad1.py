import matplotlib.pyplot as plt
F=float(input("Unesi iznos sile u Njutnima:"))
m=float(input("Unesi masu cestice u kilogramima:"))
a=F/m
dt=1
v=0
x=0
t=0
akceleracija=[]
brzina=[]
pomak=[]
vrijeme=[]
for i in range(10):
    v=v+ a*dt
    x=x+v*dt
    t+=dt
    brzina.append(v)
    pomak.append(x)
    vrijeme.append(t)
    akceleracija.append(a)
plt.subplot(311)
plt.plot(vrijeme,pomak)
plt.title("x-t graf")
plt.subplot(312)
plt.plot(vrijeme,brzina,"r")
plt.title("v-t graf")
plt.subplot(313)
plt.plot(vrijeme,akceleracija,"g")
plt.title("a-t graf")
plt.show()
