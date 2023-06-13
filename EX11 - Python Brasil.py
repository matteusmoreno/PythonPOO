'''
Implemente uma classe chamada Carro com as seguintes propriedades:

    Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no
    tanque.
    O consumo é especificado no construtor e o nível de combustível inicial é 0.
    Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de
    combustível no tanque de gasolina.
    Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    Forneça um método adicionarGasolina( ), para abastecer o tanque
'''


class Carro:
    def __init__(self, consumo=15, nivel_combustivel=0):
        self.consumo = consumo
        self.nivel_combustivel = nivel_combustivel

    def andar(self, distancia):
        if self.nivel_combustivel >= (self.consumo * distancia):
            self.nivel_combustivel -= (self.consumo * distancia)
        else:
            print('Não há combustível para percorrer esta distância')

    def adicionar_gasolina(self, qtd_gasolina):
        self.nivel_combustivel += qtd_gasolina

    def obter_gasolina(self):
        return print(f'A quantidade de gasolina no tanque é de: {self.nivel_combustivel:.1f}l')


meu_carro = Carro()
meu_carro.obter_gasolina()
meu_carro.adicionar_gasolina(450)
meu_carro.obter_gasolina()



