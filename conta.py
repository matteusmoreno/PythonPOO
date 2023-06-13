'''
Implemente um sistema de conta bancária. Ele deve possuir um atributo privado do tipo double para armazenar o saldo
da conta, que inicia com 0.0 por padrão, e 4 métodos públicos:
o método setSaldo, para definir o saldo da conta, o método getSaldo, que retorna o valor do saldo, um método depositar
, para acrescentar um valor ao saldo, e um método sacar , para retirar um valor do saldo.
Considere que o saldo da conta não pode ser negativo.
'''


class Conta:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print('O Saldo não pode ser negativo')
            self.__saldo = 0
        else:
            self.__saldo = novo_saldo

    def depositar(self, valor_deposito):
        if valor_deposito < 0:
            return print('Valor para depósito deve ser positivo')
        else:
            self.__saldo += abs(valor_deposito)

    def sacar(self, valor_saque):
        novo_saldo = self.__saldo - valor_saque
        if novo_saldo < 0:
            return print('Quantia indisponível na sua conta')
        else:
            self.__saldo -= valor_saque




