class BichinhoVirtual:

    def __init__(self, nome, idade, fome='satisfeito', saude='bem', humor='feliz'):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = humor

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def alterar_fome(self, fome):
        self.fome = fome
        self.calcular_humor()
        return self.fome

    def alterar_saude(self, saude):
        self.saude = saude
        self.calcular_humor()
        return self.saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        return self.idade

    def calcular_humor(self):
        if self.fome == 'satisfeito' and self.saude == 'bem':
            self.humor = 'feliz'
        elif (self.fome == 'faminto' and self.saude == 'bem') or (self.fome == 'satisfeito' and self.saude == 'doente'):
            self.humor = 'tristinho'
        else:
            self.humor = 'triste'

        return self.humor


if __name__ == '__main__':
    tamagoshi = BichinhoVirtual('Tamagoshi', 2)
    print(tamagoshi.__dict__)
    tamagoshi.alterar_saude('doente')
    print(tamagoshi.__dict__)
    tamagoshi.alterar_saude('bem')
    print(tamagoshi.__dict__)
    tamagoshi.alterar_idade(3)
    tamagoshi.alterar_fome('faminto')
    print(tamagoshi.__dict__)
    tamagoshi.alterar_saude('doente')
    print(tamagoshi.__dict__)
    

