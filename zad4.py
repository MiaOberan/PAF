from math import sqrt
def udaljenost_tocke(x1,y1,x2,y2,r):
    x=(x1-x2)**2+(y1-y2)**2
    d=sqrt(x)
    if d<r:
        print(f"točka je unutar kružnice, a udaljenost je {d}")
    elif d==r:
        print(f"točka je na kružnici, a udaljenost je {d}")
    else:
        print(f"tocka je izvan kruznice, a udaljenost je {d}")
udaljenost_tocke(2,3,1,4,5)