class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.crescer(anos)
        self.idade += anos
        return self.idade, self.altura

    def engordar(self, peso):
        self.peso += peso
        return self.peso

    def emagrecer(self, peso):
        self.peso -= peso
        return self.peso

    def crescer(self, anos):
        for i in range(self.idade, self.idade+anos+1):
            print(
                f'Agora {pessoa1.nome} possui {i} anos e {pessoa1.altura} cm de altura!')
            if i <= 21:
                self.altura += 0.5

        return self.altura


if __name__ == '__main__':
    pessoa1 = Pessoa('João', 10, 100, 189.5)

    print(f'Agora {pessoa1.nome} possui {pessoa1.envelhecer(3)[0]} anos e {pessoa1.envelhecer(3)[1]} cm de altura!')
    print(f'Agora {pessoa1.nome} possui {pessoa1.engordar(15)} kg.')
    print(f'Agora {pessoa1.nome} possui {pessoa1.emagrecer(10)} kg.')
    print(f'Agora {pessoa1.nome} possui {pessoa1.crescer(4)} cm.')

