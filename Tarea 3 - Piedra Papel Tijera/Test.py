from PiedraClass import Piedra
from PapelClass import Papel
from TijeraClass import Tijera

def test_PiedraGanar():
    papelPrueba = Papel()
    piedraPrueba = Piedra()

    assert papelPrueba.ganar(piedraPrueba) == "Gana Papel"