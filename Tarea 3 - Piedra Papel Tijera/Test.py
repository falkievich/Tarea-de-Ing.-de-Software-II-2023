from PiedraClass import Piedra
from PapelClass import Papel
from TijeraClass import Tijera

def test_PiedraPartidos():
    piedraPrueba = Piedra()
    piedraPrueba2 = Piedra()
    papelPrueba = Papel()
    tijeraPrueba = Tijera()
    

    assert piedraPrueba.ganar(piedraPrueba2) == "Empate"    #Piedra vs Piedra
    assert piedraPrueba.ganar(papelPrueba) == "Pierde"      #Piedra vs Papel
    assert piedraPrueba.ganar(tijeraPrueba) == "Gana"       #Piedra vs Tijera

def test_PapelPartidos():
    piedraPrueba = Piedra()
    papelPrueba = Papel()
    papelPrueba2 = Papel()
    tijeraPrueba = Tijera()
    

    assert papelPrueba.ganar(piedraPrueba) == "Gana"        #Papel vs Piedra
    assert papelPrueba.ganar(papelPrueba2) == "Empate"      #Papel vs Papel
    assert papelPrueba.ganar(tijeraPrueba) == "Pierde"       #Papel vs Tijera

def test_TijeraPartidos():
    piedraPrueba = Piedra()
    papelPrueba = Papel()
    tijeraPrueba = Tijera()
    tijeraPrueba2 = Tijera()
    

    assert tijeraPrueba.ganar(piedraPrueba) == "Pierde"    #Tijera vs Piedra
    assert tijeraPrueba.ganar(papelPrueba) == "Gana"      #Tijera vs Papel
    assert tijeraPrueba.ganar(tijeraPrueba2) == "Empate"       #Tijera vs Tijera