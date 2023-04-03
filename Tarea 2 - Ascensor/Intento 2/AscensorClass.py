from PisoClass import Piso

class Ascensor:
    def __init__(self, piso):
        self.piso = piso
        self.historial = []
        
    def getPisoActual(self):
        return self.piso

    def verHistorial(self):
        return self.historial
    
    def verHistorialString(self):
        lista = []

        for piso in self.historial:
            lista.append(piso.getNombre())

        return lista

    def setPiso(self, piso):
        self.piso = piso
    
    def __bajarHasta__(self, piso):

        pisoActual = self.getPisoActual()
        pisoEvitarHistorial = self.getPisoActual()
        historial = []

        while pisoActual != piso and pisoActual != None:

            if pisoActual != pisoEvitarHistorial:
                historial.append(pisoActual)

            pisoActual = pisoActual.getPisoAbajo()

        if pisoActual == piso:
            historial.append(pisoActual)

        if pisoActual == None:
            historial = []

        return historial

    def __subirHasta__(self, piso):
        pisoActual = self.getPisoActual()
        pisoEvitarHistorial = self.getPisoActual()
        historial = []

        while pisoActual != piso and pisoActual != None:

            if pisoActual != pisoEvitarHistorial:
                historial.append(pisoActual)

            pisoActual = pisoActual.getPisoArriba()

        if pisoActual == piso:
            historial.append(pisoActual)

        if pisoActual == None:
            historial = []

        return historial
    
    def irA(self, piso):
        
        if self.__subirHasta__(piso) != []:
            self.historial.extend(self.__subirHasta__(piso))
            self.setPiso(piso)

        elif self.__bajarHasta__(piso) != []:
            self.historial.extend(self.__bajarHasta__(piso))
            self.setPiso(piso)

        else:
            return None
        
               
