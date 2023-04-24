import ElementClass 

class Papel(ElementClass.Element):
    def __init__(self):         
        pass

    def ganarPiedra(self):
        return "Pierde"

    def ganarPapel(self):
        return "Empate"

    def ganarTijera(self):
        return "Gana"
    
    def ganar(self, objeto):
        return objeto.ganarPapel()