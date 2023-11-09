from Cuenta import Cuenta
#CONSTANTE CEVALLOS RICHARD

class CuentaAhorros(Cuenta):
    def __init__(self, credito, debito, numero, nombre, saldo, interes):
        super().__init__(credito, debito, numero, nombre, saldo)
        self._interes = interes

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, interes):
        self._interes = interes


    def calcular_credito(self):
        return self.saldo + self.credito

    def calcular_debito(self):
        if self.saldo - self.debito >= 0:
            return self.saldo - self.debito
        else:
            print("Fondos insuficientes. No se puede completar la transacción.")

    def pagar_interes(self):
        interes_generado = self.saldo * self.interes
        return self.saldo + interes_generado

    def pagar_cheque(self):
        if self.saldo - self.tienechequera >= 0:
            return self.saldo - self.tienechequera
        else:
            print("Fondos insuficientes para pagar el cheque.")
    def mostrar_saldo(self):
        print(f"Saldo: {self._saldo}")

    def __str__(self):
        return f'CuentaAhorro: {self.__dict__.__str__()}'

if __name__=='__main__':
    # Ejemplo de uso
    Calcredito = CuentaAhorros(550,200,85555, 'luis', 1000, 200)
    print(Calcredito)
    print(f'Valor saldo crédito: {Calcredito.calcular_credito()}')
if __name__=='__main__':
    # Ejemplo de uso
    Caldebito = CuentaAhorros(550,200,85555, 'luis', 1000, 200)
    print(Caldebito)
    print(f'Valor saldo débito: {Caldebito.calcular_debito()}')
if __name__=='__main__':
    # Ejemplo de uso
    Calinteres = CuentaAhorros(550,200,85555, 'luis', 1000, 200)
    print(Calinteres)
    print(f'Valor pagar interés: {Calinteres.pagar_interes()}')