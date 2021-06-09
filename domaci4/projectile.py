import math as m 
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0,kut,masa,x0,y0,A,Cx,Oblik,rho = 1.225,dt = 0.01):
        kut = (kut/180)*m.pi
        self.kut = kut
        self.v0 = v0
        self.vx = v0*m.cos(self.kut)
        self.vxr = v0*m.cos(self.kut)
        self.vy = v0*m.sin(self.kut)
        self.vyr = v0*m.sin(self.kut)
        self.masa = masa
        self.polozaj_x = x0
        self.polozaj_x_r = x0
        self.polozaj_y = y0
        self.polozaj_y_r = y0 
        self.povrsina = A
        self.koeficjent = Cx
        self.oblik = Oblik
        self.polozaj = y0
        self.polozaj_r = y0
        self.rho = rho 
        self.dt = dt
        self.pomak_x = [x0]
        self.pomak_y = [y0]

    def delete(self):
        del self.vx
        del self.vy
        del self.polozaj_x
        del self.polozaj_y
        del self.polozaj
        self.pomak_x.clear()
        self.pomak_y.clear()

    def reset(self):
        del self.v0
        del self.polozaj_r
        del self.polozaj
        del self.oblik
        del self.kut
        del self.vx
        del self.vy
        del self.masa
        del self.polozaj_x
        del self.polozaj_y
        del self.povrsina
        del self.koeficjent
        del self.rho
        del self.dt
        del self.polozaj_x_r
        del self.polozaj_y_r
        del self.vxr
        del self.vyr
        self.pomak_x.clear()
        self.pomak_y.clear()