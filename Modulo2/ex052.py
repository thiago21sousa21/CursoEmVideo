# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele
# é ou não um número primo.

from time import sleep

n = int(input('Digite um número a ser verificado se é primo: '))

divisoes = 0
for c in range(2,n):
    if n % c == 0:
        divisoes+=1
if divisoes < 1:
    print("O número é primo!")
else:
    print(f"O número não é primo pois além do 1 ele foi dividivo mais {divisoes} vezes")