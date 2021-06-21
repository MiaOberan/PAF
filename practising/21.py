import matplotlib.pyplot as plt
F = float(input('Unesi iznos sile: '))
m = float(input('Unesi masu cestice: '))
a = F/m
d_t = 0.5
v = 0
x = 0
t = 0
akceleracije = []
brzine = []
pomaci = []
vrijeme = []
for i in range(20):
    v = v + a*d_t
    x = x + v*d_t
    t += d_t
    brzine.append(v)
    pomaci.append(x)
    vrijeme.append(t)
    akceleracije.append(a)

plt.subplot(311)
plt.plot(vrijeme,pomaci)
plt.title('x-t graf')
plt.subplot(312)
plt.plot(vrijeme, brzine, 'r')
plt.title('v-t graf')
plt.subplot(313)
plt.plot(vrijeme, akceleracije, 'g')
plt.title('a-t graf')

plt.show()
