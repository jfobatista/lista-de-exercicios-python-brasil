"""
Exercício 06 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.

    >>> calcular_media((7, 7, 7, 7),(5, 7, 7, 2),(1, 10, 7, 8),(2, 2, 3, 7),(4, 2, 7, 4),(4, 7, 8, 10),(7, 1, 1, 1),(7, 2, 7, 7),(10, 8, 7, 7),(7, 9, 7, 7))
    A quantidade de alunos aprovados é: 4

"""


def calcular_media(*conjunto_de_notas):
    alunos_aprovados = 0
    for alunos in conjunto_de_notas:
        soma_notas = 0
        for nota in alunos:
            soma_notas += nota
        if soma_notas / 4 >= 7:
            alunos_aprovados += 1

    print(f'A quantidade de alunos aprovados é: {alunos_aprovados}')
