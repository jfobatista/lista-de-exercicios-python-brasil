"""
Exercício 15 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;

    >>> from secao_04_exercicios_lista import ex_15_informações_sobre_elementos
    >>> numeros = [10, 15, -1, 20, 10, 1, 2, 5, 6, 12, 13]
    >>> ex_15_informações_sobre_elementos.input = lambda k: numeros.pop()
    >>> ex_15_informações_sobre_elementos.calcula_elementos()


"""

def calcula_elementos():
    numero = int(input('Informe um numero:'))
    lista = []
    soma_valores = valor_menor_que_sete = quantidade_valores = 0
    while numero != -1:
        lista.append(numero)
        soma_valores += numero
        quantidade_valores += 1
        if numero < 7:
            valor_menor_que_sete += 1
        numero = int(input('Informe um numero:'))

    media_valores = soma_valores/quantidade_valores

    print(lista)
    lista_reversa = list(reversed(lista))
    print(lista_reversa)
    print(soma_valores)
    print(media_valores)

    for i in lista:
        if i < media_valores:
            print(i)
    print(valor_menor_que_sete)
    print('Fim do programa')
