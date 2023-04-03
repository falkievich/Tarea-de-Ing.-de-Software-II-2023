from unittest.mock import Mock          #Librería Mock
import hashlib                          #Librería para realizar el Hash
from datetime import datetime           #Librería de tiempo
from IBloqueClass import IBloque

class MiClaseMock(Mock, IBloque):
    def __init__(self):
        super().__init__(spec=IBloque)
        
    pass

def test_GenerarGenesis():
    #Datos para mi utilización=  2023-03-22 18:00:00.00 |   0.genesis2023-03-22 18:00:00.00

    #Creo mi objeto Mock y defino las variables de mi Interfaz Bloque
    mock_object = MiClaseMock()
    mock_object.index =0
    mock_object.hashInterno = "."
    mock_object.nonce = ""
    mock_object.transaccion = "genesis"
    mock_object.time = "."         

    #Creo mi tiempo utulizando la librería datetime, en este caso debo introducir los valores manualmente, de lo contrario, la libreria tomaria la fecha actual.
    fecha = datetime(2023, 3, 22, 18, 0, 0, 0)
    cadena_fecha = fecha.strftime("%Y-%m-%d %H:%M:%S") + ".00"
    mock_object.time = cadena_fecha

    #Compruebo si string de tiempo es igual al solicitado
    assert mock_object.time == "2023-03-22 18:00:00.00"

    #Convierto los datos enteros a cadena y posteriormente uno todos mis datos en una sola cadena
    cadena1_Index = str(mock_object.index)
    cadenaFinal = "{}{}{}{}{}".format(cadena1_Index, mock_object.hashInterno, mock_object.nonce, mock_object.transaccion, mock_object.time)

    #Compruebo que la cadena arma sea igual a la cadena pedida
    assert cadenaFinal == "0.genesis2023-03-22 18:00:00.00"

    # Convertimos la cadena Final a bytes
    cadena_bytes = cadenaFinal.encode()

    # Creamos un objeto hash sha256
    objetoHash = hashlib.sha256()

    # Actualizamos el hash con los bytes de la cadena
    objetoHash.update(cadena_bytes)

    # Obtenemos el código hash en formato hexadecimal
    codigoHash = objetoHash.hexdigest()

    # Compruebo de que el hash generado sea igual al solicitado
    assert codigoHash == "0ce5d49a6c34a7369cdebba7df81bad47c3ca2842e7a8d92061e74e33193e55a"
        



