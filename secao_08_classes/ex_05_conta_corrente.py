class ContaCorrente():
    def __init__(self, numero_da_conta, nome, saldo = 0):
        self.numero = numero_da_conta
        self.nome = nome
        self.saldo = saldo

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


if __name__ == '__main__':
    pessoa = ContaCorrente(154, 'João')
    print(pessoa.numero, pessoa.nome, pessoa.saldo)
    novo_nome = 'Alisson'
    try:
        pessoa.alterar_nome(novo_nome)
    except:
        print('Deu alguma coisa errada.')
    else:
        print('Nome alterado com sucesso!')

    try:
        pessoa.deposito(400)
    except:
        print('Que')
    else:
        print(f'Depósito realizado com success.')

    try:
        pessoa.saque(500)
    except TypeError:
        print('Não foi possível realizar o saque.')
    except:
        print('Deu outro trem ai')
    else:
        print('Saque realizado com sucesso.')

    print(pessoa.numero, pessoa.nome, pessoa.saldo)
