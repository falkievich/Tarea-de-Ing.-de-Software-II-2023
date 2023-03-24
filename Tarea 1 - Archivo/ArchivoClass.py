import ElementoBaseClass 

class Archivo(ElementoBaseClass.ElementoBase):          #Herencia de Elemento Base

    def __init__(self, nombre, tamano):

        ElementoBaseClass.ElementoBase.__init__(self, nombre, tamano)       #Constructor de Elemento Base
        pass
