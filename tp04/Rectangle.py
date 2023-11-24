


class Rectangle:
    """
    La class Rectangle
    """
    
    def __init__(self,longueur,largeur):
        """
        Constructeur de Rectangle

        Args:
            longueur (_type_): _description_
            largeur (_type_): _description_
        """
        self.__longueur = longueur
        self.__largeur = largeur
    
    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self,value):
        self.__longueur = value
    
    @largeur.setter
    def largeur(self,value):
        self.__largeur = value
        
    def get_surface(self):
        return self.__largeur*self.__longueur

    # r1==r2
    # r1.__eq__(r2)
    def __eq__(self, o):
        return  self.__longueur == o.__longueur and self.__largeur == o.__largeur
    
    def __str__(self):
        return f"{__class__.__name__} {self.__longueur=},{self.__largeur=}"
    
    # longueur = property(get_longueur,set_longueur)
    # largeur = property(get_largeur,set_largeur)