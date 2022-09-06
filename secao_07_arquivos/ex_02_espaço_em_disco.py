"""
    Exercício 02 da seção de Arquivos da Python Brasil:
    https://wiki.python.org.br/ExerciciosArquivos

    Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
    contendo um relatório dos endereços IP válidos e inválidos.

    >>> gera_relatorio()
    a
"""

def calcula_bytes_em_megabytes(bytes):
    return round(bytes/1048576,2)

def gera_relatorio():
    arquivo_usuarios = open('C:\\Desktop\\usuarios.txt','r')
    usuarios = []
    for linha in arquivo_usuarios:
        linha = linha.replace('\n','')
        usuarios.append([linha[:16], linha[16:]])

    espaco_total_ocupado = 0
    espaco_medio_ocupado = 0

    for usuario in usuarios:
        for indice, valor in enumerate(usuario):
            if indice == 1:
                valor = int(valor)
                usuario[indice] = calcula_bytes_em_megabytes(valor)
                espaco_total_ocupado += usuario[indice]
            
    espaco_medio_ocupado = round(espaco_total_ocupado/len(usuarios), 2)

    mb = 'MB'

    relatorio = open('C:\\Desktop\\relatorio.txt','w')
    relatorio.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    relatorio.write('------------------------------------------------------------------------\n')
    relatorio.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    relatorio.write('\n')
    
    for indice, usuario in enumerate(usuarios):
        relatorio.write(f'{indice+1:<3} {usuario[0]} {usuario[1]:>10} {mb:>1} {usuario[1]/espaco_total_ocupado:>13.2%}\n')
    
    relatorio.write('\n')
    relatorio.write(f'Espaço total ocupado: {espaco_total_ocupado} MB\n')
    relatorio.write(f'Espaço médio ocupado: {espaco_medio_ocupado} MB\n')