class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_valor_lado(self, lado):
        self.lado = lado

    def retornar_valor_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2


quadrado = Quadrado(2)
print(quadrado.retornar_valor_lado())
print(quadrado.calcular_area())
print(quadrado.mudar_valor_lado(5))
print(quadrado.retornar_valor_lado())
print(quadrado.calcular_area())
