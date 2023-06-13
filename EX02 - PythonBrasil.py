''''
Classe Quadrado: Crie uma classe que modele um quadrado:
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área
'''


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_valor_lado(self, novo_lado):
        self.lado = novo_lado

    def __str__(self):  # Retornar valor do lado
        return f'O valor do lado do quadrado é {self.lado}cm'

    def calcular_area(self):
        area = self.lado * self.lado
        return f'A área do quadrado é {area}cm²'


quadrado1 = Quadrado(24)

print(quadrado1.__str__())
print(quadrado1.calcular_area())
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
quadrado1.mudar_valor_lado(36)
print(quadrado1.__str__())
print(quadrado1.calcular_area())