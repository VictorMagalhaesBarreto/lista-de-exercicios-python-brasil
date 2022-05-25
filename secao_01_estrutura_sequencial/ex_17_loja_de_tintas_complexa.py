"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 18 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.7 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 3.3 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 3.3 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.3 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.9 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.9 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    tm = float(input(''))
    qtdtl=tm=(tm+tm*0.1)/6;
    qtdl = (round(qtdtl+qtdtl*0.1))/18
    sl= (round(qtdl)*18)-qtdtl
    pl = round(qtdl) * 80
    qtdg =(round(qtdtl+qtdtl*0.1))/3.6
    sg= (round(qtdg)*3.6)-qtdl
    pg= round(qtdg)*25
    qtdm=sl/3.6
    pm=pl+(qtdm*25)
    sm= ((qtdm*3.6)+(qtdl*18))-qtdtl



    # 1 litro - 6 metros
    # Lata 18 litros (R$80,00), galão 3.6 litros (R$25,00)

    print(f'Você deve comprar {round(qtdtl)} litros de tinta.')
    print(f'Você pode comprar {round(qtdl)} lata(s) de 18 litros a um custo de R$ {pl}. Vão sobrar {sl}  litro(s) de tinta.')
    print(f'Você pode comprar {round(qtdg)} lata(s) de 3.6 litros a um custo de R$ {pg}. Vão sobrar {sg}  litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {round(qtdl)} lata(s) de 18 litros e {round(qtdm)} galão(ões) de 3,6 a um custo de R$ {pm}. Vão sobrar {sm} litro(s) de tinta.')