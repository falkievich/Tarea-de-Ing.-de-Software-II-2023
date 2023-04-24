from AscensorClass import Ascensor
from PisoClass import Piso

def test_ViajarPiso1a5():
    piso1 = Piso("Piso 1")
    piso2 = Piso("Piso 2")
    piso3 = Piso("Piso 3")
    piso4 = Piso("Piso 4")
    piso5 = Piso("Piso 5")

    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)

    ascensorPrueba = Ascensor(piso1)
    ascensorPrueba.irA(piso5)
    
    historial = ["Piso 2", "Piso 3", "Piso 4", "Piso 5"]
    assert historial == ascensorPrueba.verHistorialString()


def test_ViajarPiso5a1():
    piso1 = Piso("Piso 1")
    piso2 = Piso("Piso 2")
    piso3 = Piso("Piso 3")
    piso4 = Piso("Piso 4")
    piso5 = Piso("Piso 5")

    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)

    ascensorPrueba = Ascensor(piso5)
    ascensorPrueba.irA(piso1)
    
    historial = ["Piso 4", "Piso 3", "Piso 2", "Piso 1"]
    assert historial == ascensorPrueba.verHistorialString()

def test_ViajarPiso1a4a2():
    piso1 = Piso("Piso 1")
    piso2 = Piso("Piso 2")
    piso3 = Piso("Piso 3")
    piso4 = Piso("Piso 4")

    piso1.setPisoArriba(piso2)
    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)

    ascensorPrueba = Ascensor(piso1)
    ascensorPrueba.irA(piso4)

    historial = ["Piso 2", "Piso 3", "Piso 4"]
    assert historial == ascensorPrueba.verHistorialString()

    ascensorPrueba.irA(piso2)

    historial = ["Piso 2", "Piso 3", "Piso 4", "Piso 3", "Piso 2"]
    assert historial == ascensorPrueba.verHistorialString()

def test_ViajarPiso6a2a3():
    piso1 = Piso("Piso 1")
    piso2 = Piso("Piso 2")
    piso3 = Piso("Piso 3")
    piso4 = Piso("Piso 4")
    piso5 = Piso("Piso 5")
    piso6 = Piso("Piso 6")

    piso2.setPisoArriba(piso3)
    piso3.setPisoArriba(piso4)
    piso4.setPisoArriba(piso5)
    piso5.setPisoArriba(piso6)

    ascensorPrueba = Ascensor(piso6)
    ascensorPrueba.irA(piso2)

    historial = ["Piso 5", "Piso 4", "Piso 3", "Piso 2"]
    assert historial == ascensorPrueba.verHistorialString()

    ascensorPrueba.irA(piso3)

    historial = ["Piso 5", "Piso 4", "Piso 3", "Piso 2", "Piso 3"]
    assert historial == ascensorPrueba.verHistorialString()