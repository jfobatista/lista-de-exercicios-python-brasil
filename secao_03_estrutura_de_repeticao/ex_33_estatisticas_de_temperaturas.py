"""
Exercício 33 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

Mostre a média com uma casa decimal.

    >>> calcular_estatisticas()
    'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    >>> calcular_estatisticas(1)
    'Maior temperatura: 1. Menor temperatura: 1. Média: 1.0'
    >>> calcular_estatisticas(1, 2)
    'Maior temperatura: 2. Menor temperatura: 1. Média: 1.5'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior temperatura: 2. Menor temperatura: -1. Média: 0.7'


"""


def calcular_estatisticas(*temperaturas) -> str:
    """Escreva aqui em baixo a sua solução"""


    if not temperaturas:
        return 'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    else:
        lista = temperaturas
        temperatura_total = 0
        maior = menor = lista[0]
        for i in lista:
            temperatura_total += i
            if i > maior:
                maior = i
            if menor > i:
                menor = i
        media = temperatura_total / len(lista)

        return f'Maior temperatura: {maior}. Menor temperatura: {menor}. Média: {media:.1f}'
