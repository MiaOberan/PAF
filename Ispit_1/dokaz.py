import modul as m
objekt1= m.Bullet(5,6)
objekt2=m.Bullet(8,10)
objekt1.change_y0(2)
print("Pocetna visina prvog objekta je sada: {}".format(objekt1.y))
objekt1.change_v0(3)
print("Pocetna brzina prvog objekta je sada: {} ms^-1".format(objekt1.v))
