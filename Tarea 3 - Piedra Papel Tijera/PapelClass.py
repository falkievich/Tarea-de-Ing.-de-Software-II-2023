import ElementClass 


class Papel(ElementClass.Element):
    def __init__(self):         
        pass


    def ganarPiedra(self, piedra):
        return "Gana Papel"

    def ganarPapel(self, papel):
        return "Empate"

    def ganarTijera(self, tijera):
        return "Gana Tijera"
    
    def ganar(self, objeto):
        return objeto.ganaPapel()
