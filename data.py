'''Crie uma classe chama Data

. Essa classe deve apresentar os seguintes atributos privados:

    dia – número inteiro que varia de 1 até 31;
    mês – número inteiro que varia de 1 até 12;
    ano – número inteiro positivo.

Esses atributos devem ser inicializados com o valor 1.

Também deve conter os seguintes métodos públicos:

    setData – Recebe valores para dia, mês e ano como parâmetros e altera os valores dos atributos caso os valores
    recebidos sejam válidos;
    getDia – Retorna o dia;
    getMes – Retorna o mês;
    getAno – Retorna o ano.
'''


class Data:
    def __init__(self, dia=1, mes=1, ano=1):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, valor_dia):
        if 1 <= valor_dia <= 31:
            self.__dia = valor_dia
        else:
            print('Dia Inválido')

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, valor_mes):
        if 1 <= valor_mes <= 12:
            self.__mes = valor_mes
        else:
            print('Mês Inválido')

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor_ano):
        if valor_ano > 0:
            self.__ano = valor_ano
        else:
            print('Ano Inválido')

    def data_valida(self):
        return print(f'Data: {self.__dia}/{self.__mes}/{self.__ano}')


data_casamento = Data()
data_casamento.dia = 7
data_casamento.mes = 12
data_casamento.ano = -989
data_casamento.data_valida()
