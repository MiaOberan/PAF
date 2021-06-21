import matplotlib.pyplot as plt
def odredi_pravac(x1,y1,x2,y2, znak):
    x_koordinate = [x1,x2]
    y_koordinate = [y1,y2]
    plt.plot(x_koordinate,y_koordinate)
    if znak == 0:
        plt.show()
    elif znak == 1:
        naziv = input('Unesite naziv slike: ' )
        plt.savefig(f'{naziv}.pdf')
    

odredi_pravac(2,4,-1,-3,1)
