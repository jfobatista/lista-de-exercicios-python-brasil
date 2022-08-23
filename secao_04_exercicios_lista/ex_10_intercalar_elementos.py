"""
Exercício 10 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

    >>> intercala_elementos()
    [1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19, 10, 20]

"""

def intercala_elementos():

    vetor_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    vetor_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    vetor_intercalado = []
    for i in range(len(vetor_2)):
        vetor_intercalado.append(vetor_1[i])
        vetor_intercalado.append(vetor_2[i])
    print(vetor_intercalado)