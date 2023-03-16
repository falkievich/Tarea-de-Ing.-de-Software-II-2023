import ElementoBaseClass

class Carpeta(ElementoBaseClass.ElementoBase):              #Herencia de Elemento Base
    def __init__(self, nombre, tamano):
        
        ElementoBaseClass.ElementoBase.__init__(self, nombre, tamano)       #Constructor de Elemento Base
        self.lista = []

    def guardarEnCarpeta(self, objeto):
        self.lista.append(objeto)
        self.tamano += objeto.tamano

 


    

  

