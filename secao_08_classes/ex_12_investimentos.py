class ContaInvestimento:
    def __init__(self, numero_da_conta, nome, juros, saldo=0):
        self.numero = numero_da_conta
        self.nome = nome
        self.saldo = saldo
        self.juros = juros

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposito(self, valor_depositado):
        self.saldo += valor_depositado
        return self.saldo

    def saque(self, valor_sacado):
        if self.saldo < valor_sacado:
            raise TypeError
        self.saldo -= valor_sacado
        return self.saldo

    def adicione_juros(self, meses):
        for i in range(0, meses):
            self.saldo += self.saldo * (self.juros/100)
        return f'O seu novo saldo é de {self.saldo}.'


if __name__ == '__main__':
    pessoa = ContaInvestimento(154, 'João', 10)
    print(pessoa.numero, pessoa.nome, pessoa.saldo)
    novo_nome = 'Alisson'
    try:
        pessoa.alterar_nome(novo_nome)
    except:
        print('Deu alguma coisa errada.')
    else:
        print('Nome alterado com sucesso!')

    try:
        valor_deposito = pessoa.deposito(1000)
    except:
        print('Que')
    else:
        print(f'Depósito de R$ {valor_deposito} realizado com successo.')

    try:
        valor_saque = pessoa.saque(5000)
    except TypeError:
        print('Não foi possível realizar o saque.')
    except:
        print('Deu outro trem ai')
    else:
        print(f'Saque de R$ {valor_saque} realizado com sucesso.')
    try:
        meses = int(input('Por quantos meses você deseja investir? '))
    except:
        print('Digite um valor inteiro válido!')
    else:
        print(pessoa.adicione_juros(meses))

    print(pessoa.numero, pessoa.nome, pessoa.saldo)
