# Exercício Python 102: Crie um programa que tenha uma função fatorial()
#  que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show,
#  que será um valor lógico (opcional)
#  indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    result = 1
    numeros = []
    for n in range(num):
        result *= n+1
        numeros.append(str(n+1))
        
    if show:
        print(f'{' x '.join(numeros)} = {result}')
    else:
        print(result)

fatorial(4, True)