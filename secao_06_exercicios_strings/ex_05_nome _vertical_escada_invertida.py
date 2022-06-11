"""
Exercício 05 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

    >>> inverter_escada('CAMARGUINHO')
    CAMARGUINHO
    CAMARGUINH
    CAMARGUIN
    CAMARGUI
    CAMARGU
    CAMARG
    CAMAR
    CAMA
    CAM
    CA
    C
    >>> inverter_escada('ENZO PASCOAL')
    ENZO PASCOAL
    ENZO PASCOA
    ENZO PASCO
    ENZO PASC
    ENZO PAS
    ENZO PA
    ENZO P
    ENZO
    ENZ
    EN
    E

"""


def inverter_escada(nome:str):
    """Escreva aqui em baixo a sua solução"""
    lista_letras = [v for v in nome]
    letras_descartadas = ''
    for i in range(len(lista_letras)-1, -1, -1):
        letra_atual = lista_letras[i]
        if letra_atual == ' ':
            pass
        else:
            saida = "".join(lista_letras)
            print(saida)
        lista_letras.pop(i)

