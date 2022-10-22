class Funcionario:
    def __init__(self, nome, salario=0):
        self.nome = nome
        self.salario = salario

    def mostrar_nome(self):
        return self.nome

    def mostrar_salario(self):
        return self.salario

    def alterar_salario(self, porcentagem):
        self.salario += self.salario * porcentagem / 100
        return self.salario


if __name__ == '__main__':

    while True:
        nome = str(input('Informe seu Nome: '))
        try:
            for i in nome:
                if i.isnumeric():
                    raise Exception
        except:
            print('Seu nome está correto?')
        else:
            break

    salario = float(input('Salário: '))
    funcionario = Funcionario(nome, salario)
    print(funcionario.mostrar_nome(), funcionario.mostrar_salario())
    print(f'Seu novo salário é de {funcionario.alterar_salario(10)}.')
