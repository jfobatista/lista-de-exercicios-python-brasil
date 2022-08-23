"""
Exercício 11 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia três vetores com 10 elementos cada. Gere um quarto vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos três outros vetores.

    >>> intercala_elementos()
    [1, 11, 21, 2, 12, 22, 3, 13, 23, 4, 14, 24, 5, 15, 25, 6, 16, 26, 7, 17, 27, 8, 18, 28, 9, 19, 29, 10, 20, 30]

"""

def intercala_elementos():
    vetor_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    vetor_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    vetor_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    vetor_intercalado = []
    for i in range(len(vetor_2)):
        vetor_intercalado.append(vetor_1[i])
        vetor_intercalado.append(vetor_2[i])
        vetor_intercalado.append(vetor_3[i])
    print(vetor_intercalado)