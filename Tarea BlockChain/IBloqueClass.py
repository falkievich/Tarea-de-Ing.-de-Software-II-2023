from abc import ABC, abstractmethod

class IBloque(ABC):

    index = 0
    hash = "1"
    hashInterno = "."
    nonce = ""
    transaccion = "datos"
    time = "tiempo"