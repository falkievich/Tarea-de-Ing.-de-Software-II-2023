class ElementoBase:

    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
        

    """def printear(self):     #Prueba sacar lluego
        print("nombre =", self.nombre)
        print("tamaño=", self.tamano) """
        
    
    def obtenerTamano(self, objeto):
        return objeto.tamano    #MAL


