import ElementoBaseClass

class Foto(ElementoBaseClass.ElementoBase):         #Herencia de Elemento Base

    def __init__(self, nombre, tamano, dimesion):
        
        ElementoBaseClass.ElementoBase.__init__(self, nombre, tamano)       #Constructor de Elemento Base
        self.dimension = dimesion
        pass

