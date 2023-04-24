import ElementClass 

class Piedra(ElementClass.Element):
    def __init__(self):         
        pass

    def ganarPapel(self):
        return "Gana"
    
    def ganarTijera(self):
        return "Pierde"
    
    def ganarPiedra(self):
        return "Empate"
    
    def ganar(self, objeto):
        return objeto.ganarPiedra()
