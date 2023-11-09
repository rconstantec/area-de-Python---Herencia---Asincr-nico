from Cuenta import Cuenta
#CONSTANTE CEVALLOS RICHARD
class CuentaCorriente(Cuenta):
    def __init__(self, credito, debito, numero, nombre, saldo, tienechequera):
        super().__init__(credito, debito, numero, nombre, saldo)
        self._tienechequera = tienechequera

    @property
    def tienechequera(self):
        return self._tienechequera

    @tienechequera.setter
    def tienechequera(self, tienechequera):
        self._tienechequera = tienechequera

    def calcular_credito(self):
        return self.saldo + self.credito

    def calcular_debito(self):
        if self.saldo - self.debito >= 0:
            return self.saldo - self.debito
        else:
            print("Fondos insuficientes. No se puede completar la transacción.")

    def pagar_cheque(self):
        if self.saldo - self.tienechequera >= 0:
            return self.saldo - self.tienechequera
        else:
            print("Fondos insuficientes para pagar el cheque.")

    def pagar_interes(self):
        interes_generado = self.saldo * self.interes
        return self.saldo + interes_generado

    def mostrar_saldo(self):
        print(f"Saldo: {self.saldo}")

    def __str__(self):
        return f'CuentaCorriente: {self.__dict__.__str__()}'


if __name__=='__main__':
    # Ejemplo de uso
    Calcredito = CuentaCorriente(550,200,85555, 'luis', 1000, 400)
    print(Calcredito)
    print(f'Valor saldo crédito: {Calcredito.calcular_credito()}')
if __name__=='__main__':
    # Ejemplo de uso
    Caldebito = CuentaCorriente(550,200,85555, 'luis', 1000, 400)
    print(Caldebito)
    print(f'Valor saldo débito: {Caldebito.calcular_debito()}')
if __name__=='__main__':
    # Ejemplo de uso
    Calcheque = CuentaCorriente(550,200,85555, 'luis', 1000, 400)
    print(Calcheque)
    print(f'Valor pagar cheque: {Calcheque.pagar_cheque()}')