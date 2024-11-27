# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120


numero = int( input("Digite um número a ser calculado o seu fatorial: "))
copy_numero = numero
multiplicador = 1
expressao = f'{numero}'
while numero > 0:
    multiplicador*=numero
    numero-=1
    expressao+=f' x {numero}'
print(f"{copy_numero}! = {expressao[:len(expressao)-4]} = {multiplicador}")
