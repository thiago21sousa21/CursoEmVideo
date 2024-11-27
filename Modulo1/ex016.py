#Crie um programa que leia um número qualquer pelo teclado e mostre a sua porção inteira

import math

numero = float(input('Digite um numero: '))

porcao_inteira = math.floor(numero)

print('a porção inteira desse número é: {}'.format(porcao_inteira))
