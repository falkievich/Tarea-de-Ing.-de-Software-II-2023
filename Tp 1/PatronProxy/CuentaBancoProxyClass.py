from ICuentaBancoClass import ICuentaBanco
from CuentaBancoRealClass import CuentaBancoReal

class CuentaBancoProxy(ICuentaBanco):
    def __init__(self):
        self.cuentaBanco = None
        

    def retirarDinero(self, cuenta, cantidad):
        if self.cuentaBanco == None:
            self.cuentaBanco = CuentaBancoReal(cuenta.nombreCuenta, cuenta.saldo)
            return self.cuentaBanco.retirarDinero(cuenta, cantidad)
        
        else:   
            return self.cuentaBanco.retirarDinero(cuenta, cantidad)
    
    def depositarDinero(self, cuenta, cantidad):
        if self.cuentaBanco == None:
            self.cuentaBanco = CuentaBancoReal(cuenta.nombreCuenta, cuenta.saldo)
            return self.cuentaBanco.depositarDinero(cuenta, cantidad)
        
        else:
            return self.cuentaBanco.depositarDinero(cuenta, cantidad)

    def mostrarSaldo(self, cuenta):
        if self.cuentaBanco == None:
            self.cuentaBanco = CuentaBancoReal(cuenta.nombreCuenta, cuenta.saldo)
            return  self.cuentaBanco.mostrarSaldo(cuenta)
        
        else:
            return  self.cuentaBanco.mostrarSaldo(cuenta)