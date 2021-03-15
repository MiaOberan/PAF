import matplotlib.pyplot as plt
def odredi_pravac(x1,y1,x2,y2, znak):
    xkoordinate=[x1,x2]
    ykoordinate=[y1,y2]
    if znak==0:
        plt.show()
    elif znak==1:
        naziv=input("Unesite naziv slike:")
        plt.savefig(f"{naziv}.pdf")
    plt.plot(xkoordinate,ykoordinate, 'go--', linewidth=2, markersize=12)
    plt.show()
odredi_pravac(3,4,5,7,1)
