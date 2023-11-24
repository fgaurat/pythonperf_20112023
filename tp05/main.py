from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle
from ICalcGeo import ICalcGeo

def show_surface(o:ICalcGeo):
    print(o.surface)

def main():
    c = Carre(5)
    c.cote = 3
    print(c.surface)
    print(c)
    print(50*'-')
    ce = Cercle(5)
    print(ce.surface)
    
    r = Rectangle(5,2)
    print(r.surface)
    
    show_surface(c)
    show_surface(ce)
    show_surface(r)
if __name__=='__main__':
    main()
