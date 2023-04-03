class AscensorClass:

    def __init__(self, pisoActual):
        self.pisoActual = pisoActual
        self.listaPiso = ["piso 0", "piso 1", "piso 2", "piso 3", "piso 4", "piso 5"]
        self.historial = []

    def subir(self, pisoIr):
        indice = self.listaPiso.index(self.pisoActual)
        while self.pisoActual != pisoIr:
            indice = indice +1
            self.historial.append( self.listaPiso[indice] )
            self.pisoActual = self.listaPiso[indice]
        
        return self.pisoActual
    
    def bajar(self, pisoIr):
        indice = self.listaPiso.index(self.pisoActual)

        while self.pisoActual != pisoIr:
            indice = indice -1
            self.historial.append( self.listaPiso[indice] )
            self.pisoActual = self.listaPiso[indice]
        
        return self.pisoActual

        
        
            


                
                
