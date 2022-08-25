"""
    Exercício 05 da seção de listas da Python Brasil:
    https://wiki.python.org.br/ExerciciosFuncoes

    Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
    que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do
    imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

    >>> somaImposto(300, 10)
    '330'

    >>> somaImposto(500,5)
    '525'
"""


def somaImposto(custo, taxaImposto):

    return f'{custo + (custo * taxaImposto / 100):.0f}'
