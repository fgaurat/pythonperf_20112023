from Rectangle import Rectangle

class Carre(Rectangle):
    
    def __init__(self,cote):
        super().__init__(cote, cote)
        self.__cote=cote
        
    @property
    def cote(self):
        return self.__cote        
    
    @cote.setter
    def cote(self,value):
        self.longueur = self.largeur = value
        self.__cote = value
                
    def __str__(self):
        return f"{__class__.__name__} {self.__cote=}"
        
        