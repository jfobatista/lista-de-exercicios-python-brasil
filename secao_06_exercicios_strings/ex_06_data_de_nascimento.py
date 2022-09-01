"""
    Exercício 06 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

    Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por
    extenso.

    >>> data_por_extenso('12/09/1995')
    Você nasceu em 12 de Setembro de 1995.

"""


def data_por_extenso(data):
    data = data.split('/')
    dia = data[0]
    mes = int(data[1])
    ano = data[2]

    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
             ]

    print(f'Você nasceu em {dia} de {meses[mes - 1]} de {ano}.')