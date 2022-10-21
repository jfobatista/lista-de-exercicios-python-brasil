class Carro:
    def __init__(self, consumo, quantidade_combustivel = 0):
        self.consumo = consumo
        self.quantidade_combustivel = quantidade_combustivel

    def adicionar_combustivel(self, combustivel_adicionado):
        self.quantidade_combustivel += combustivel_adicionado
        return f'Você abasteceu {combustivel_adicionado} litros de combustível e agora ' \
               f'possui {self.quantidade_combustivel} litros.'

    def calcula_autonomia(self):
        autonomia = self.consumo * self.quantidade_combustivel
        return autonomia

    def andar(self, kilometros):
        autonomia = self.calcula_autonomia()
        if kilometros > autonomia:
            quantidade_combustivel_necessaria = (kilometros - autonomia) / self.consumo
            raise Exception(quantidade_combustivel_necessaria, kilometros)

        combustivel_gasto = round(kilometros / self.consumo, 2)
        self.quantidade_combustivel -= combustivel_gasto
        return f'Para andar {kilometros}km foram gastos {combustivel_gasto} litros ' \
               f'de combustível. O total restante no tanque é de ' \
               f'{self.quantidade_combustivel} litros'


if __name__ == '__main__':
    meuFusca = Carro(15)
    print(meuFusca.adicionar_combustivel(20))
    print(meuFusca.adicionar_combustivel(20))
    print(meuFusca.calcula_autonomia())
    try:
        print(meuFusca.andar(330))
    except Exception as erro:
        (qtd, km) = erro.args
        print(f'Não será possível completar a viagem, pois para rodar {km}km '
              f'seriam necessários mais {qtd} litros de combustível.')
