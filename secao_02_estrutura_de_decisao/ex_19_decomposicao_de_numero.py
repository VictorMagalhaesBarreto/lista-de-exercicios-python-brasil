"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""

    if numero<0:
        print("'O número precisa ser positivo'")
    elif numero>=1000:
        print("'O número precisa ser menor que 1000'")
    else:
        centena = numero // 100
        dezena = (numero-centena*100) // 10
        unidade= (numero-((centena*100)+(dezena*10))) // 1
        if centena==1 and dezena ==1 and unidade == 0:
            print(f"'{numero} = {centena} centena e {dezena} dezena'")
        elif centena > 1 and dezena > 1 and unidade == 0:
            print(f"'{numero} = {centena} centenas e {dezena} dezenas'")
        elif centena > 1 and dezena == 1 and unidade == 0:
            print(f"'{numero} = {centena} centenas e {dezena} dezena'")
        elif centena == 1 and dezena > 1 and unidade == 0:
            print(f"'{numero} = {centena} centena e {dezena} dezenas'")
        elif centena == 0 and dezena == 1 and unidade == 1:
            print(f"'{numero} = {dezena} dezena e {unidade} unidade'")
        elif centena==0 and dezena>1 and unidade>1:
            print(f"'{numero} = {dezena} dezenas e {unidade} unidades'")
        elif centena == 0 and dezena > 1 and unidade == 1:
            print(f"'{numero} = {dezena} dezenas e {unidade} unidade'")
        elif centena == 0 and dezena == 1 and unidade > 1:
            print(f"'{numero} = {dezena} dezena e {unidade} unidades'")
        elif centena == 1 and dezena == 0 and unidade == 1:
             print(f"'{numero} = {centena} centena e {unidade} unidade'")
        elif centena > 1 and dezena == 0 and unidade > 1:
            print(f"'{numero} = {centena} centenas e {unidade} unidades'")
        elif centena > 1 and dezena == 0 and unidade == 1:
            print(f"'{numero} = {centena} centenas e {unidade} unidade'")
        elif centena == 1 and dezena == 0 and unidade > 1:
            print(f"'{numero} = {centena} centena e {unidade} unidades'")
        elif centena == 1 and dezena == 1 and unidade == 1:
            print(f"'{numero} = {centena} centena, {dezena} dezena e {unidade} unidade'")
        elif centena > 1 and dezena > 1 and unidade > 1:
            print(f"'{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades'")
        elif centena > 1 and dezena == 1 and unidade == 1:
            print(f"'{numero} = {centena} centenas, {dezena} dezena e {unidade} unidade'")
        elif centena == 1 and dezena > 1 and unidade == 1:
            print(f"'{numero} = {centena} centena, {dezena} dezenas e {unidade} unidade'")
        elif centena == 1 and dezena == 1 and unidade > 1:
            print(f"'{numero} = {centena} centena, {dezena} dezena e {unidade} unidades'")
        elif centena == 1 and dezena == 0 and unidade == 0:
            print(f"'{numero} = {centena} centena'")
        elif centena > 1 and dezena == 0 and unidade == 0:
            print(f"'{numero} = {centena} centenas'")
        elif centena == 0 and dezena == 1 and unidade == 0:
            print(f"'{numero} = {dezena} dezena'")
        elif centena == 0 and dezena > 1 and unidade == 0:
            print(f"'{numero} = {dezena} dezenas'")
        elif centena == 0 and dezena == 0 and unidade == 1:
            print(f"'{numero} = {unidade} unidade'")
        elif centena == 0 and dezena == 0 and unidade > 1:
            print(f"'{numero} = {unidade} unidades'")






