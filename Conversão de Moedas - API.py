# POO, API, Classe Mãe
import requests


class ConverteMoeda:  # SuperClasse
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    def __init__(self, real=0, _dolar=float(requisicao.json()['USDBRL']['bid']),
                 _euro=float(requisicao.json()['EURBRL']['bid']), _bitcoin=float(requisicao.json()['BTCBRL']['bid'])):
        self.real = real
        self.dolar = _dolar
        self.euro = _euro
        self.bitcoin = _bitcoin


class Dolar(ConverteMoeda):
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    def __init__(self, real=0, _dolar=float(requisicao.json()['USDBRL']['bid'])):
        super().__init__(real, _dolar)

    def brl_usd(self):
        return print(f'R${self.real:.2f} é igual a US${self.real / self.dolar:.2f}')


class Euro(ConverteMoeda):
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    def __init__(self, real=0, _euro=float(requisicao.json()['EURBRL']['bid'])):
        super().__init__(real, _euro)

    def brl_eur(self):
        return print(f'R${self.real:.2f} é igual a €{self.real / self.euro:.2f}')


class Bitcoin(ConverteMoeda):
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    def __init__(self, real=0, bitcoin=float(requisicao.json()['BTCBRL']['bid'])):
        super().__init__(real, bitcoin)

    def brl_btc(self):
        return print(f'R${self.real:.2f} é igual a ₿{self.real / self.bitcoin:.9f}')


dolar = Dolar(100)
dolar.brl_usd()
euro = Euro(100)
euro.brl_eur()
btc = Bitcoin(100)
btc.brl_btc()

