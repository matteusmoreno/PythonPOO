'''
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias
    para o local.
'''


class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_valor_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retorna_valor_lados(self):  # Retorna valor dos lados
        return f'O terreno tem {self.lado_a:.2f}m x {self.lado_b:.2f}m'

    def calcula_area(self):
        area = self.lado_a * self.lado_b
        return area

    def calcula_perimetro(self):
        perimetro = (self.lado_a + self.lado_b) * 2
        return perimetro


comprimento = float(input('Informe a COMPRIMENTO do terreno (m): '))
largura = float(input('Infrme a LARGURA do terreno (m): '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

terreno = Retangulo(comprimento, largura)

print(terreno.retorna_valor_lados())
print(f'A ÁREA do terreno é de {terreno.calcula_area():.2f}m²')
print(f'O PERÍMETRO do terreno é de {terreno.calcula_perimetro():.2f}m')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
terreno.mudar_valor_lados(38, 54)
print(terreno.retorna_valor_lados())
print(f'A ÁREA do terreno é de {terreno.calcula_area():.2f}m²')
print(f'O PERÍMETRO do terreno é de {terreno.calcula_perimetro():.2f}m')