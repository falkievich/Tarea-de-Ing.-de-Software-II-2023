from ElementoBaseClass  import ElementoBase
from FotoClass  import Foto
from CarpetaClass import Carpeta
from ArchivoClass import Archivo


def test_DeberaCrear_Archivo():
    archivoPrueba = Archivo("LOL", "30 KB")

def test_DeberaCrear_Foto():
    fotoPrueba = Foto("Thiago", "300 KB", "1980x1080")

def test_DeberaCrear_Carpeta():
    carpetaPrueba = Carpeta("Nueva carpeta", "1 KB")

def test_VerTamano_Archivo():
    archivoPrueba = Archivo("LOL", "30 KB")
    assert archivoPrueba.obtenerTamano(archivoPrueba) == "30 KB"

def test_VerTamano_Foto():
    fotoPrueba = Foto("Thiago", "300 KB", "1980x1080")
    assert fotoPrueba.obtenerTamano(fotoPrueba) == "300 KB"

def test_VerTamano_Carpeta():
    carpetaPrueba = Carpeta("Nueva carpeta", "1 KB")
    assert carpetaPrueba.obtenerTamano(carpetaPrueba) == "1 KB"

def test_Guardar_Archivo():
    listaPrueba =[]

    carpeta = Carpeta("Carpeta donde guardo cosas", "1KB")
    archivoPrueba = Archivo("LOL", "30 KB")

    assert carpeta.guardarEnCarpeta(archivoPrueba) == listaPrueba.append(archivoPrueba)

def test_Guardar_Foto():
    listaPrueba =[]

    carpeta = Carpeta("Carpeta donde guardo cosas", "1KB")
    fotoPrueba = Foto("Thiago", "300 KB", "1980x1080")

    assert carpeta.guardarEnCarpeta(fotoPrueba) == listaPrueba.append(fotoPrueba)

def test_Guardar_Carpeta():
    listaPrueba =[]

    carpeta = Carpeta("Carpeta donde guardo cosas", "1KB")
    carpetaPrueba = Carpeta("Nueva carpeta", "1 KB")

    assert carpeta.guardarEnCarpeta(carpetaPrueba) == listaPrueba.append(carpetaPrueba)

def test_Guardar_MuchasCosas():
    listaPrueba =[]

    carpeta = Carpeta("Carpeta donde guardo cosas", "1KB")
    archivoPrueba = Archivo("LOL", "30 KB")
    carpetaPrueba = Carpeta("Nueva carpeta", "1 KB")

    assert carpetaPrueba.guardarEnCarpeta(archivoPrueba) == listaPrueba.append(archivoPrueba)      #Guardo un archivo dentro de una carpeta 1
    assert carpeta.guardarEnCarpeta(carpetaPrueba) == listaPrueba.append(carpetaPrueba)     #Guardo la carpeta 1 dentro de una carpeta 2
    

    



    