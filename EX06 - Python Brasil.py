'''
Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o
número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.
'''


class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self):
        if 0 <= self.volume <= 99:
            novo_volume = self.volume + 1
            self.volume = novo_volume
            return print(f'Volume: {self.volume}')
        elif self.volume > 99:
            self.volume = 100
            return print(f'Volume: {self.volume}')

    def diminuir_volume(self):
        if 1 <= self.volume <= 100:
            novo_volume = self.volume - 1
            self.volume = novo_volume
            return print(f'Volume: {self.volume}')
        elif self.volume < 1:
            self.volume = 0
            return print(f'Volume: {self.volume}')

    def mostrar_canal(self):
        return print(f'Canal: {self.canal}')


tv_quarto = TV(12, 98)
tv_quarto.aumentar_volume()
tv_quarto.aumentar_volume()
tv_quarto.aumentar_volume()
tv_quarto.mostrar_canal()