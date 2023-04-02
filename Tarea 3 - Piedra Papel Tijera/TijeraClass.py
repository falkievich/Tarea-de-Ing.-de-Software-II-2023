import ElementClass 

class Tijera(ElementClass.Element):
    def __init__(self):         
        pass
    
    def ganarTijera(self):
        return "Empate"
    
    def ganarPapel(self):
        return "Pierde"
    
    def ganarPiedra(self):
        return "Gana"
    
    def ganar(self, objeto):
        return objeto.ganarTijera()