from ICuentaBancoClass import ICuentaBanco

class CuentaBancoReal(ICuentaBanco):
    def __init__(self, nombreCuenta, saldo):
        self.nombreCuenta = nombreCuenta
        self.saldo = saldo

 
    def retirarDinero(self, cuenta, cantidad):
        saldoActual = cuenta.saldo
        if (saldoActual >= cantidad):
            saldoActual = saldoActual - cantidad
            cuenta.saldo = saldoActual
            return saldoActual
        else:
            return "Su saldo actual es insuficiente"
    

    def depositarDinero(self, cuenta, cantidad):
        cuenta.saldo = cuenta.saldo + cantidad
        return cuenta.saldo

    def mostrarSaldo(self, cuenta):
        return ("Su saldo es: $" + str(cuenta.saldo) ) 