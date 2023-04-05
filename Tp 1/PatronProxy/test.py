from CuentaBancoRealClass import CuentaBancoReal
from CuentaBancoProxyClass import CuentaBancoProxy

def test_CrearCuentaReal():
    cuentaRealPrueba = CuentaBancoReal("Cuenta Thiago", 150)
    assert cuentaRealPrueba.nombreCuenta == "Cuenta Thiago"
    assert cuentaRealPrueba.saldo == 150

def test_MostrarSaldo():
    cuentaRealPrueba = CuentaBancoReal("Cuenta Thiago", 150)
    cuentaProxyPrueba = CuentaBancoProxy()

    assert cuentaProxyPrueba.mostrarSaldo(cuentaRealPrueba) == "Su saldo es: $150"

def test_RetirarDinero():
    cuentaRealPrueba = CuentaBancoReal("Cuenta Thiago", 150)
    cuentaProxyPrueba = CuentaBancoProxy()

    assert cuentaProxyPrueba.retirarDinero(cuentaRealPrueba, 50) == 100
    assert cuentaProxyPrueba.mostrarSaldo(cuentaRealPrueba) == "Su saldo es: $100"

def test_RetirarDineroInsuficiente():
    cuentaRealPrueba = CuentaBancoReal("Cuenta Thiago", 150)
    cuentaProxyPrueba = CuentaBancoProxy()

    assert cuentaProxyPrueba.retirarDinero(cuentaRealPrueba, 500) == "Su saldo actual es insuficiente"

def test_DepositarDinero():
    cuentaRealPrueba = CuentaBancoReal("Cuenta Thiago", 150)
    cuentaProxyPrueba = CuentaBancoProxy()

    assert cuentaProxyPrueba.depositarDinero(cuentaRealPrueba, 320) == 470
    assert cuentaProxyPrueba.mostrarSaldo(cuentaRealPrueba) == "Su saldo es: $470"

def test_ConjuntoDeTests():
    cuentaRealPrueba = CuentaBancoReal("Cuenta Thiago", 150)
    cuentaProxyPrueba = CuentaBancoProxy()

    assert cuentaProxyPrueba.mostrarSaldo(cuentaRealPrueba) == "Su saldo es: $150"

    assert cuentaProxyPrueba.retirarDinero(cuentaRealPrueba, 50) == 100
    assert cuentaProxyPrueba.mostrarSaldo(cuentaRealPrueba) == "Su saldo es: $100"

    assert cuentaProxyPrueba.depositarDinero(cuentaRealPrueba, 320) == 420
    assert cuentaProxyPrueba.mostrarSaldo(cuentaRealPrueba) == "Su saldo es: $420"

    assert cuentaProxyPrueba.retirarDinero(cuentaRealPrueba, 500) == "Su saldo actual es insuficiente"