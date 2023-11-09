from abc import ABC, abstractmethod
#CONSTANTE CEVALLOS RICHARD
class Cuenta(ABC):
    def __init__(self, credito, debito, numero, nombre, saldo):
        self._numero = numero
        self._nombre = nombre
        self._saldo = saldo
        self._credito = credito
        self._debito = debito
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo > 0:
            self._saldo = saldo
        else:
            print("El valor del saldo debe ser mayor que cero.")

    @property
    def credito(self):
        return self._credito

    @credito.setter
    def credito(self,Nuevocredito):
        self._credito = Nuevocredito

    @property
    def debito(self):
        return self._debito

    @debito.setter
    def debito(self, Nuevodebito):
        self._debito = Nuevodebito

    @abstractmethod
    def mostrar_saldo(self):
        pass

    @abstractmethod
    def calcular_credito(self):
        pass

    @abstractmethod
    def calcular_debito(self):
        pass

    @abstractmethod
    def pagar_interes(self):
        pass

    @abstractmethod
    def pagar_cheque(self):
        pass


    def __str__(self):
        return f'Cuenta {self.__dict__.__str__()}'