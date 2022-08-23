"""
Exercício 04 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

    >>> quantidade_de_consoantes('a','b','c','d','e','f','g','h','i','j')
    Consoantes: 7
    >>> quantidade_de_consoantes('a','a','a','a','e','a','g','a','i','a')
    Consoantes: 1
    >>> quantidade_de_consoantes('b','b','c','d','x','f','g','h','z','j')
    Consoantes: 10

"""


def quantidade_de_consoantes(*letras):
    """Escreva aqui em baixo a sua solução"""
    qtd_consoantes = 0
    for i in letras:
        if i not in ('a', 'e', 'i', 'o', 'u'):
            qtd_consoantes += 1
    print(f'Consoantes: {qtd_consoantes}')