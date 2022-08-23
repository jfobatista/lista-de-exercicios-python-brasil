"""
Exercício 08 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

    >>> mostrar_dados((12, 1.6), (13, 1.7), (25, 1.9),(46, 1.74), (22, 2.02))
    (22, 2.02)
    (46, 1.74)
    (25, 1.9)
    (13, 1.7)
    (12, 1.6)

"""


def mostrar_dados(*pessoas):
    for i in range(len(pessoas), 0, -1):
        print(pessoas[i - 1])
