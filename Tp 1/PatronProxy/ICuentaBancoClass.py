from abc import ABC, abstractmethod

class ICuentaBanco(ABC):

    @abstractmethod
    def retirarDinero(self, cuenta, cantidad):
        """
        """
    
    @abstractmethod
    def depositarDinero(self, cuenta, cantidad):
        """
        """
    
    @abstractmethod
    def mostrarSaldo(self, cuenta):
        """
        """

    