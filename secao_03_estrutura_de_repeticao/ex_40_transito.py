"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil habitantes.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil habitantes.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil habitantes é de 900.0 acidentes.
"""
from math import ceil


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    def calcular_indice_acidentes(cidade):
        return cidade[2] * 1000 / cidade[1]
    maior_indice = menor_indice = numero_veiculos = numero_acidentes = cidades_pequenas = 0
    nome_maior_indice = nome_menor_indice = ''
    for x in cidades:
        indice = calcular_indice_acidentes(x)
        if maior_indice < indice:
            maior_indice = indice
            nome_maior_indice = x[0]
        else:
            menor_indice = indice
            nome_menor_indice = x[0]
        numero_veiculos += x[1]
        if x[1] <= 150_000:
            numero_acidentes += x[2]
            cidades_pequenas += 1
    media_veiculos = numero_veiculos / len(cidades)
    media_acidentes = numero_acidentes / cidades_pequenas
    print(f'O maior índice de acidentes é de {nome_maior_indice}, com {maior_indice:.1f} acidentes por mil habitantes.')
    print(f'O menor índice de acidentes é de {nome_menor_indice}, com {menor_indice:.1f} acidentes por mil habitantes.')
    print(f'O média de veículos por cidade é de {media_veiculos:.0f}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil habitantes é de {media_acidentes:.1f} acidentes.')
