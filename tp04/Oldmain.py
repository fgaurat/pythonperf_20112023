from Rectangle import Rectangle

def main():
    r = Rectangle(5,8)
    
    # print(r._Rectangle__longueur)
    # print(r._Rectangle__largeur)
    lng = r.get_longueur()
    lrg = r.get_largeur()
    print(lng,lrg)
    

    r.set_longueur(12)
    print(r.get_longueur()) # 12

    r.set_largeur(54)
    print(r.get_largeur()) # 54

    print(r.get_surface()) # 648
    print(50*'-')
    r1 = Rectangle(5,8)
    r2 = Rectangle(5,8)
    
    if r1 == r2:
        print("ok")
    else:
        print("ko")
    print(50*'-')
    r1 = Rectangle(5,8)
    s = str(r1)
    print(s)
    
    print(50*'-')
    r1 = Rectangle(5,8)
    r1.longueur = -12
    print(r1.longueur)
    
    
    
if __name__=='__main__':
    main()
