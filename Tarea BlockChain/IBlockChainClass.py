from abc import ABC, abstractmethod

class IBlockChain(ABC):

    @abstractmethod
    def generarGenesis(self):
        """
        """

    @abstractmethod
    def guardarBloque(self, bloque):
        """
        """