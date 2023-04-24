class Piso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pisoAbajo = None
        self.pisoArriba = None


    def obtenerPiso(self):
        return self.nombre
    
    def setPisoArriba(self, piso):
        self.pisoArriba = piso
        piso.pisoAbajo = self
    
    def setPisoAbajo(self, piso):
        self.pisoAbajo = piso
        piso.pisoArriba = self

    def getPisoArriba(self):
        return self.pisoArriba
    
    def getPisoAbajo(self):
        return self.pisoAbajo
    
    def getNombre(self):
        return self.nombre
