import projectile as ptl
import matplotlib.pyplot as plt
import numpy as np

def ovisnost_dometa_o_koef_Cd():
    D_lista = []
    Cd_lista = list(np.linspace(0,5, num = 1000))

    p = ptl.projectile()

    for cd in Cd_lista:
        p.init(10,10,60,0,0,1.2,cd,0.5,0.01)      
        D = p.range()
        D_lista.append(D)
        p.reset()

    plt.figure("Graf 1")
    plt.plot(Cd_lista,D_lista,"k", linewidth=3, label = "Euler")
    plt.xlabel("Koeficijent trenja")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o koef. trenja")
    plt.legend()
    plt.show()

def ovisnost_dometa_o_masi():
    D_lista = []
    m_lista = list(np.linspace(0.01,1.5, num = 1000))

    p = ptl.projectile()

    for m in m_lista:
        p.init(m,10,60,0,0,1.2,1,0.5,0.01) 
        D = p.range()
        D_lista.append(D)
        p.reset()

    plt.figure("Graf 1")
    plt.plot(m_lista,D_lista,"m", linewidth=3, label = "Euler")
    plt.xlabel("Masa [kg]")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o masi")
    plt.legend()
    plt.show()

ovisnost_dometa_o_koef_Cd()
ovisnost_dometa_o_masi()