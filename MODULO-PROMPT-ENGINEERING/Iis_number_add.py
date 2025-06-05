"""crie uma função que receba um número inteiro e retorne se ele é par ou ímpar, se ele for impar retorne true, se elefor par retorne false.
Caso o usuario não passa um número inteiro retorne erro que não é um numero inteiro."""

def is_number_odd(number):
    if type(number) != int:
       raise ValueError( "Erro: não é um número inteiro")
    """ se o numero for zero me retorne um erro não é um numero desejavel"""
    if number == 0:
        raise ValueError("Erro: zero não é um número desejável")
    
    if number % 2 == 0:
        return False
    else:
        return True