class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_em_reais):
        quantidade_abastecida = round(valor_em_reais / self.valor_litro, 2)
        if self.quantidade_combustivel < quantidade_abastecida:
            raise ValueError(f'{self.tipo_combustivel}')
        self.quantidade_combustivel -= quantidade_abastecida
        return f'Você abasteceu {quantidade_abastecida} litros de {self.tipo_combustivel} ' \
               f'no valor de R$ {valor_em_reais}. A quantidade de' \
               f' {self.tipo_combustivel} ' \
               f'é de {self.quantidade_combustivel} litros. '

    def abastecer_por_litro(self, quantidade_litros):
        if self.quantidade_combustivel < quantidade_litros:
            raise ValueError(f'{self.tipo_combustivel}')
        valor_em_reais = round(quantidade_litros * self.valor_litro, 2)
        self.quantidade_combustivel -= quantidade_litros
        return f'Você abasteceu {quantidade_litros} litros de {self.tipo_combustivel} ' \
               f'no valor de R$ {valor_em_reais}. A quantidade de' \
               f' {self.tipo_combustivel} ' \
               f'é de {self.quantidade_combustivel} litros. '

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        return f'O novo valor por litro do combustível {self.tipo_combustivel}' \
               f' é de R$ {self.valor_litro}.'

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
        return self.tipo_combustivel

    def adicionar_combustivel(self, quantidade_combustivel):
        self.quantidade_combustivel += quantidade_combustivel
        return f'A nova quantidade de {self.tipo_combustivel} é de ' \
               f'{self.quantidade_combustivel:.2f} litros.'


if __name__ == '__main__':
    try:
        gasolina = BombaCombustivel('Gasolina', 4.89, 20)
    except:
        print('Aconteceu algo')

    try:
        alcool = BombaCombustivel('Álcool', 3.59, 50)
    except:
        print('Algo deu errado')

    print(gasolina.__dict__)
    print(gasolina.alterar_valor(4.99))
    print(gasolina.abastecer_por_valor(50))
    try:
        print(gasolina.abastecer_por_litro(15))
    except ValueError:
        print(f'A bomba não possui a quantidade de {gasolina.tipo_combustivel} '
              f'disponível.')
    print(gasolina.adicionar_combustivel(30))
    print(gasolina.__dict__)
    print('-'*30)
    print(alcool.__dict__)
    try:
        print(alcool.abastecer_por_valor(50))
    except ValueError as erro:
        print(f'A bomba não possui a quantidade de {erro} disponível.')
    print(alcool.alterar_valor(3.49))
    try:
        print(alcool.abastecer_por_valor(200))
    except ValueError as exece:
        print(f'A bomba não possui a quantidade de {exece} disponível.')
    print(alcool.__dict__)
