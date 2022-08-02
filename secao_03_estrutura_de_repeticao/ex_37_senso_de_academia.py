"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    nome = str(input('Infome o nome do aluno'))
    altura = str(input('Informe a altura do aluno'))
    peso = str(input('Informe o peso do aluno'))
    altura = int(altura)
    peso = int(peso)
    altura_total = peso_total = 0
    altura_total += altura
    peso_total += peso
    numero_de_alunos = 1
    nome_mais_gordo = nome_mais_magro = nome_mais_alto = nome_mais_baixo = nome
    peso_mais_gordo = peso_mais_magro = peso
    altura_mais_alto = altura_mais_baixo = altura
    nome = str(input('Infome o nome do aluno'))
    while nome != '0':
        altura = str(input('Informe a altura do aluno'))
        peso = str(input('Informe o peso do aluno'))
        altura = int(altura)
        peso = int(peso)
        altura_total += altura
        peso_total += peso
        numero_de_alunos += 1

        if altura > altura_mais_alto:
            altura_mais_alto = altura
            nome_mais_alto = nome
        elif altura < altura_mais_baixo:
            altura_mais_baixo = altura
            nome_mais_baixo = nome
        if peso > peso_mais_gordo:
            peso_mais_gordo = peso
            nome_mais_gordo = nome
        elif peso < peso_mais_magro:
            peso_mais_magro = peso
            nome_mais_magro = nome
        nome = str(input('Infome o nome do aluno'))

    print(f'Cliente mais alto: {nome_mais_alto}, com {altura_mais_alto} centímetros')
    print(f'Cliente mais baixo: {nome_mais_baixo}, com {altura_mais_baixo} centímetros')
    print(f'Cliente mais magro: {nome_mais_magro}, com {peso_mais_magro} kilos')
    print(f'Cliente mais gordo: {nome_mais_gordo}, com {peso_mais_gordo} kilos')
    print('--------------------------------------------------')
    print(f'Media de altura dos clientes: {altura_total / numero_de_alunos:.1f} centímetros')
    print(f'Media de peso dos clientes: {peso_total / numero_de_alunos:.1f} kilos')
