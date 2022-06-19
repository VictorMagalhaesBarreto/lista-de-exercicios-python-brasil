"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    data_separada= data.split('/')
    tuple(data_separada)
    if data_separada=='' or len(data_separada) !=3:
        print("'Data inválida'")
    else:
            day, month, year = data_separada
            day= int(day)
            month= int(month)
            year= int(year)
            if month in range(1, 13):
                if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
                    print("'Data válida'")
                elif month in [4, 6, 9, 11] and day in range(1, 31):
                    print("'Data válida'")
                elif month == 2 and ((day in range(1, 29)) or (year % 4 == 0 and year % 400 == 0 and year % 100 == 0 and day in range(1, 30))):
                    print("'Data válida'")
                else:
                    print("'Data inválida'")
            else:
                print("'Data inválida'")




