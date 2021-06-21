from math import sqrt
import matplotlib.pyplot as plt
def udaljenost_tocke(x1,y1,x2,y2,r):
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    kruznica = plt.Circle((x2,y2),r, color ='r')
    plt.gca().add_artist(kruznica)
    plt.plot(x1,y1, 'bo')    
    x = (x1-x2)**2 + (y1-y2)**2
    d = sqrt(x)
    nacin = int(input('Unesi 1 za prikaz slike, a 2 za spremanje'))
    if nacin == 1:
        plt.show()
    elif nacin == 2:
        naziv = input('Unesite naziv slike: ' )
        plt.savefig(f'{naziv}.pdf')


    epsilon = 0.01
    if d < r:
        print(f'Točka je unutar kružnice, a udaljenost je {d}')
    elif r-epsilon < d < r+epsilon:
         print(f'Točka je na kružnici, a udaljenost je {d}')
    else:
         print(f'Točka je izvan kružnice, a udaljenost je {d}')
    


udaljenost_tocke(5,3,4,3,2)
