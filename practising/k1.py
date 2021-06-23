import VertikalniHitac as vert 

vh1 = vert.VertikalniHitac(18,11)

#d
import VertikalniHitac as vert 

vh1 = vert.VertikalniHitac(5,10)
vh2 = vert.VertikalniHitac(7,8)

vh1.change_y0(11)
vh2.change_v0(4)

print("Pocetna visina prvog objekta je sada: {} m \nPocetna brzina drugog objekta je sada: {} ms^-1".format(vh1.y,vh2.v))

#3
import VertikalniHitac as vert
import matplotlib.pyplot as plt 

vh1 = vert.VertikalniHitac(10,10)
dt = 0.01

ylist, vlist, tlist = vh1.run_event(dt)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(tlist, ylist)
ax1.set(xlabel='t [s]', ylabel='y [m]')
ax2.plot(tlist, vlist)
ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
plt.show()

#4
import VertikalniHitac as vert 

dt1 = 0.01
dt2 = 0.05

vh1 = vert.VertikalniHitac(10,10)
maxy = vh1.max_height(dt1)
vh1.return_to_start()
t = vh1.duration(dt2)
print("Max visina je: {} m \nVrijeme trajanja je: {} s".format(maxy,t))

#5
import VertikalniHitac as vert
import matplotlib.pyplot as plt

dt  = 0.01
k = 1.5
vh1 = vert.VertikalniHitac(10,10)

maxy = vh1.max_height(dt)
vh1.return_to_start()
maxyar = vh1.max_height_with_ar(dt,k)
vh1.return_to_start()

t = vh1.duration(dt)
vh1.return_to_start()
tar = vh1.duration_with_ar(dt,k)
vh1.return_to_start()

ylist1, vlist1, tlist1 = vh1.run_event(dt)
vh1.return_to_start()

ylist2, vlist2, tlist2 = vh1.run_event_with_ar(dt,k)
vh1.return_to_start()

print("Max visina bez otpora zraka je: {} m \nMax visina sa otporom zraka je: {} m".format(maxy,maxyar))
print("Vrijeme trajanja hitca bez otpora zraka je: {} s\nVrijeme trajanja hitca sa otporom zraka je: {} s".format(t,tar))

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(tlist1, ylist1)
ax1.set(xlabel='t [s]', ylabel='y [m]')
ax2.plot(tlist1, vlist1)
ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
plt.title("Bez otpora zraka")
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(tlist2, ylist2)
ax1.set(xlabel='t [s]', ylabel='y [m]')
ax2.plot(tlist2, vlist2)
ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
plt.title("Sa otporom zraka")
plt.show()
