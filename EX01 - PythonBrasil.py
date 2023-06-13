''''
Classe Bola: Crie uma classe que modele uma bola:
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
'''


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(f'A nova cor da bola é: {self.cor}')


bola_menino = Bola('amarela', 18, 'borracha')
print(f'Cor: {bola_menino.cor} - Circunferência: {bola_menino.circunferencia}cm - Material: {bola_menino.material}')

bola_menino.trocaCor('azul')
bola_menino.mostraCor()