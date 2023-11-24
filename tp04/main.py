from Rectangle import Rectangle
from DataRectangle import DataRectangle


def main():
    r = Rectangle(1,2)
    r.longueur = 5
    print(r.longueur)
    r1 = DataRectangle()
    print(r1.longueur) # 0
    r1.longueur = 12
    print(r1.longueur)# 12
    print(r1)# DataRectangle(longueur=12, largeur=0)

if __name__=='__main__':
    main()
