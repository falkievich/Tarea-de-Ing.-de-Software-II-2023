import ElementClass 

class Tijera(ElementClass.Element):
    def __init__(self):         
        pass
    
    def ganaTijera(self):
        return "Empate"
    
    def ganaPapel(self):
        return "Gana Papel"
    
    def ganaPiedra(self):
        return "Gana Piedra"
    
    def ganar(self, objeto):
        return objeto.ganaTijera()