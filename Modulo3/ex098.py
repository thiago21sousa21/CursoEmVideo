# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
#  que receba três parâmetros: início, fim e passo.
#  Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            a) de 1 até 10, de 1 em 1                                                                                                                                              b) de 10 até 0, de 2 em 2                                                                                                                                            c) uma contagem personalizada
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2  
# c) uma contagem personalizada

def personalizado (i, f, s):
    if s == 0:
        s = 1
    s = abs(s)

    while f > i:
        print(i, end=' ')
        i+= s
    while i > f:
        print(i, end=' ')
        i-= s



personalizado(0, 10, 0)