"""
Exercício 27 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos e devem ter ao menos um aluno.
Arredonde o valor da média para baixo.

    >>> from secao_03_estrutura_de_repeticao import ex_27_alunos_por_turma
    >>> entradas = ['1', '1']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 1
    Média de alunos por turma: 1
    >>> entradas = ['40', '40', '2']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 2
    Média de alunos por turma: 40
    >>> entradas = ['10', '20', '30', '40', '-1', '4']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 4
    Uma turma deve ter de 1 a 40 alunos, não é possível ter -1 alunos
    Média de alunos por turma: 25
    >>> entradas = ['10', '20', '30', '0', '41', '3']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 3
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 41 alunos
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 0 alunos
    Média de alunos por turma: 20

"""
from math import ceil


def calcular_media_de_alunos_por_turma():
    """Escreva aqui em baixo a sua solução"""
    quantidade_de_turmas = int(input('Informe a quantidade de turmas:'))
    print(f'Número de turmas: {quantidade_de_turmas}')
    soma_dos_alunos = verifica_turmas = 0
    while verifica_turmas < quantidade_de_turmas:
        tamanho = int(input('Informe a quantidade de alunos desta turma:'))
        if tamanho <= 0 or tamanho > 40:
            print(f'Uma turma deve ter de 1 a 40 alunos, não é possível ter {tamanho} alunos')
        else:
            soma_dos_alunos += tamanho
            verifica_turmas += 1

    media_de_alunos = ceil(soma_dos_alunos / quantidade_de_turmas)
    print(f'Média de alunos por turma: {media_de_alunos}')