"""
    Exercício 01 da seção de Arquivos da Python Brasil:
    https://wiki.python.org.br/ExerciciosArquivos

    Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
    contendo um relatório dos endereços IP válidos e inválidos.

"""


def validacao_ip():
    arquivo_ips = open('C:\Desktop\ips.txt', 'r')
    lista_com_ips_validos = []
    lista_com_ips_invalidos = []
    ip_valido = 0
    for linha in arquivo_ips:
        ip = linha.replace('\n', '').split('.')
        for numero in ip:
            numero = int(numero)
            if not (0 <= numero <= 255):
                continue
            else:
                ip_valido += 1
        if ip_valido == 4:
            lista_com_ips_validos.append(linha)
        else:
            lista_com_ips_invalidos.append(linha)
        ip_valido = 0

    arquivo_ips.close()

    arquivo_ips_validos = open('C:\Desktop\ips_validos.txt','w')

    for ip in lista_com_ips_validos:
        arquivo_ips_validos.write(ip)

    arquivo_ips_invalidos = open('C:\Desktop\ips_invalidos.txt','w')

    for ip in lista_com_ips_invalidos:
        arquivo_ips_invalidos.write(ip)

    arquivo_ips_invalidos.close()
    arquivo_ips_validos.close()