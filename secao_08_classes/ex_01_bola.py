class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)


azul = Bola('Azul',2,'Borracha')
azul.mostraCor()
azul.trocaCor('Amarela')
azul.mostraCor()
