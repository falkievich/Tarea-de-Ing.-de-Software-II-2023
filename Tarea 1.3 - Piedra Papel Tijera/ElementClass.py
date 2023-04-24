import abc

class Element():
    def __init__(self):
        pass         
        
    @abc.abstractmethod
    def ganar(self, objeto):
        pass

    @abc.abstractmethod
    def ganarPiedra(self):
        pass

    @abc.abstractmethod
    def ganarPapel(self):
        pass

    @abc.abstractmethod
    def ganarTijera(self):
        pass