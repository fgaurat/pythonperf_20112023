from Rectangle import Rectangle


def main():
    r = Rectangle()
    r1 = Rectangle(5,6)
    r2 = Rectangle(5,6)
    
    print(Rectangle._cpt)
    print(r.get_cpt())
    
    r3 = Rectangle.build_from_str("5x6")
    print(r3)
if __name__=='__main__':
    main()
