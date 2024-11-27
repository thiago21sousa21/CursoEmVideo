# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
#  que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno.

def area(comp, lar):
    print(f'A area é: {comp*lar:.2f} m²')

comp = float(input('Digite o comprimento: '))
lar = float(input('Digite a largura: '))

area(comp, lar)