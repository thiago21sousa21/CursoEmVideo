"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random

numero_aleatorio = random.randint(0,5)
choice = int(input("Tente a sorte e digite um numero entre um e 5: "))

if numero_aleatorio == choice:
    print(f"você acertou! o pc escolheu {numero_aleatorio} e voce escolheu {choice}")
else:
    print(f"\033[7;31;43mvocê errou o pc escolheu {numero_aleatorio} e você escolheu {choice}\033[m")