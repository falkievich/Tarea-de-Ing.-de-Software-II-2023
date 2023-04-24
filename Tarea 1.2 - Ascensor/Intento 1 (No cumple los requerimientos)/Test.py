from Ascensor import AscensorClass

def test_Piso0a1(): 
    listaPruba = ["piso 1"]                     #Esta lista es creada para representa la validez de la lista historial
    ascensorPrueba = AscensorClass("piso 0")    # Al ascensor se le brinda como dato en que piso está actualmente

    assert ascensorPrueba.subir("piso 1") == "piso 1"   #La función subir devuelve la variable pisoActual, esto indica que efectivamente el ascensor está en el piso indicado
    assert ascensorPrueba.historial == listaPruba

def test_Piso2a5():
    listaPruba = ["piso 3","piso 4","piso 5"]
    ascensorPrueba = AscensorClass("piso 2")

    assert ascensorPrueba.subir("piso 5") == "piso 5"
    assert ascensorPrueba.historial == listaPruba

def test_Piso2a0():
    listaPruba = ["piso 1", "piso 0"]
    ascensorPrueba = AscensorClass("piso 2")

    assert ascensorPrueba.bajar("piso 0") == "piso 0"
    assert ascensorPrueba.historial == listaPruba

def test_Piso4a1():
    listaPruba = ["piso 3", "piso 2", "piso 1"]
    ascensorPrueba = AscensorClass("piso 4")

    assert ascensorPrueba.bajar("piso 1") == "piso 1"
    assert ascensorPrueba.historial == listaPruba
    
def test_Piso1a4_4a2():
    listaPruba1 = ["piso 2", "piso 3", "piso 4"]
    listaPruba2 = ["piso 2", "piso 3", "piso 4","piso 3", "piso 2"]
    ascensorPrueba = AscensorClass("piso 1")

    assert ascensorPrueba.subir("piso 4") == "piso 4"
    assert ascensorPrueba.historial == listaPruba1

    assert ascensorPrueba.bajar("piso 2") == "piso 2"
    assert ascensorPrueba.historial == listaPruba2

def test_Piso2a3_3a5_5a2_2_4():
    listaPruba1 = ["piso 3"]
    listaPruba2 = [ "piso 3", "piso 4","piso 5"]
    listaPruba3 = [ "piso 3", "piso 4","piso 5", "piso 4", "piso 3", "piso 2"]
    listaPruba4 = [ "piso 3", "piso 4","piso 5", "piso 4", "piso 3", "piso 2", "piso 3", "piso 4"]
    ascensorPrueba = AscensorClass("piso 2")

    assert ascensorPrueba.subir("piso 3") == "piso 3"
    assert ascensorPrueba.historial == listaPruba1      #2 a 3

    assert ascensorPrueba.subir("piso 5") == "piso 5"
    assert ascensorPrueba.historial == listaPruba2      #3 a 5

    assert ascensorPrueba.bajar("piso 2") == "piso 2"  
    assert ascensorPrueba.historial == listaPruba3      #5 a 2

    assert ascensorPrueba.subir("piso 4") == "piso 4"  
    assert ascensorPrueba.historial == listaPruba4      #2 a 4

