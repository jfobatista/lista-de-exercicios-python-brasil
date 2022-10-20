class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_valor(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

    def mostrar_valor(self):
        return self.comprimento, self.largura

    def calculo_retangulo(self):
        area = self.comprimento * self.largura
        perimetro = self.comprimento * 2 + self.largura * 2

        return area, perimetro


if __name__ == '__main__':

    while True:
        try:
            lado1 = float(input('Informe o valor do comprimento do retângulo: '))
        except:
            print('\033[031mInforme um valor inteiro ou real válido.\033[m')
        else:
            break
    while True:
        try:
            lado2 = float(input('Informe o valor da largura do retângulo: '))
        except:
            print('\033[031mInforme um valor inteiro ou real válido.\033[m')
        else:
            break
    retangulo = Retangulo(lado1, lado2)

    print(retangulo.mostrar_valor())
    print(f'Area = {retangulo.calculo_retangulo()[0]} -^- Perimetro = {retangulo.calculo_retangulo()[1]}')
