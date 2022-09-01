"""
    Exercício 07 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

    Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por
    extenso.

    >>> conta_espacos_e_vogais('Voce nasceu em 12 de Setembro de 1995')
    Espaços: 7
    Vogais: 11

"""
import unidecode


def conta_espacos_e_vogais(frase):
    frase = unidecode.unidecode(frase).lower()
    frase_sem_espacos = frase.split(' ')
    numero_espacos = len(frase_sem_espacos) - 1
    numero_vogais = 0
    vogais = 'a', 'e', 'i', 'o', 'u'
    for characters in frase:
        if characters in vogais:
            numero_vogais += 1
    print(f'Espaços: {numero_espacos}\nVogais: {numero_vogais}')
