import ElementClass 

class Piedra(ElementClass.Element):
    def __init__(self):         
        pass

    def ganaPapel(self):
        return "Gana Papel"
    
    def ganaTijera(self):
        return "Gana Tijera"
    
    def ganaPiedra(self):
        return "Empate"
    
    def ganar(self, objeto):
        return objeto.ganaPiedra()
