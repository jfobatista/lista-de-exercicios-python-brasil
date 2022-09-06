"""
    Exercício 01 da seção de Arquivos da Python Brasil:
    https://wiki.python.org.br/ExerciciosArquivos

    Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
    contendo um relatório dos endereços IP válidos e inválidos.

"""


def valida_ip():
    arquivo_ips = open('ips.txt', 'r')
    lista_com_ips = []

    for linha in arquivo_ips:
        lista_com_ips.append(linha)

    print(linha)
