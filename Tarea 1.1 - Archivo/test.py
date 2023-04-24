from ElementoBaseClass  import ElementoBase
from FotoClass  import Foto
from CarpetaClass import Carpeta
from ArchivoClass import Archivo


def test_DeberaCrear_Archivo():                                         #Ejecutar Test con:    pytest .\test.py -v
    archivoPrueba = Archivo("LOL", 30 )

def test_DeberaCrear_Foto():
    fotoPrueba = Foto("Thiago", 300 , "1980x1080")

def test_DeberaCrear_Carpeta():
    carpetaPrueba = Carpeta("Nueva carpeta", 1 )

def test_VerTamano_Archivo():
    archivoPrueba = Archivo("LOL", 30 )
    assert archivoPrueba.obtenerTamano() == 30

def test_VerTamano_Foto():
    fotoPrueba = Foto("Thiago", 300, "1980x1080")
    assert fotoPrueba.obtenerTamano() == 300

def test_VerTamano_Carpeta():
    carpetaPrueba = Carpeta("Nueva carpeta", 1)
    assert carpetaPrueba.obtenerTamano() == 1

def test_Guardar_Archivo():                                         #REVISAR
    listaPrueba =[]

    carpeta = Carpeta("Carpeta donde guardo cosas", 1)
    archivoPrueba = Archivo("LOL", 30 )

    assert carpeta.guardarEnCarpeta(archivoPrueba) == listaPrueba.append(archivoPrueba)

def test_Guardar_Foto():
    listaPrueba =[]

    carpeta = Carpeta("Carpeta donde guardo cosas", 1)
    fotoPrueba = Foto("Thiago",300 , "1980x1080")

    assert carpeta.guardarEnCarpeta(fotoPrueba) == listaPrueba.append(fotoPrueba)

def test_Guardar_Carpeta():
    listaPrueba =[]

    carpeta = Carpeta("Carpeta donde guardo cosas", 1)
    carpetaPrueba = Carpeta("Nueva carpeta", 1 )

    assert carpeta.guardarEnCarpeta(carpetaPrueba) == listaPrueba.append(carpetaPrueba)

def test_Guardar_VerTamano_Archivo():
    archivoPrueba = Archivo("LOL", 30 )
    carpeta = Carpeta("Carpeta donde guardo cosas", 1)

    carpeta.guardarEnCarpeta(archivoPrueba)
    assert carpeta.obtenerTamano() == 31

def test_Guardar_VerTamano_Foto():
    fotoPrueba = Foto("Thiago",300 , "1980x1080")
    carpeta = Carpeta("Carpeta donde guardo cosas", 1)

    carpeta.guardarEnCarpeta(fotoPrueba)
    assert carpeta.obtenerTamano() == 301

def test_Guardar_VerTamano_Carpeta():
    carpetaPrueba = Carpeta("Carpeta donde guardo cosas", 10)
    carpeta = Carpeta("Carpeta donde guardo cosas", 1)

    carpeta.guardarEnCarpeta(carpetaPrueba)
    assert carpeta.obtenerTamano() == 11

def test_Guardar_MuchasCosas():

    carpeta = Carpeta("Carpeta donde guardo cosas", 1)
    ArchivoPrueba = Archivo("LOL", 30)
    carpetaPrueba = Carpeta("Nueva carpeta", 1 )

    assert carpetaPrueba.obtenerTamano() == 1
    carpetaPrueba.guardarEnCarpeta(ArchivoPrueba)       #Guardo un archivo dentro de la carpeta 1
    assert carpetaPrueba.obtenerTamano() == 31
    

    carpeta.guardarEnCarpeta(carpetaPrueba)      #Guardo la carpeta 1 dentro de la carpeta 2
    assert carpeta.obtenerTamano() == 32

    



    