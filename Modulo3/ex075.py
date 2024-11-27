# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

v1 = int(input('digite o primeiro valor: '))
v2 = int(input('digite o segundo valor: '))
v3 = int(input('digite o terceiro valor: '))
v4 = int(input('digite o quarto valor: '))

tupla_valores = (v1, v2, v3, v4)

print(f'o valor 9 apareceu {(tupla_valores).count(9)} vezes')

if 3 in tupla_valores:
    print(f'o primeiro valor tres fica na {(tupla_valores).index(3)+1}ª posição')

pares = ''

for par in tupla_valores:
    if par % 2 == 0:
        pares+=f'{par} '

print(f'Os números pares são:: {pares}')

