# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e 
# também indique o menor e o maior valor que estão na tupla.

from random import randint

aleatorios = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f' a lista é  {aleatorios}')
print(f' o menor é {sorted(aleatorios)[0]}')
print(f' o maior é {sorted(aleatorios)[4]}')

