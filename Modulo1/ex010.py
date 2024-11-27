#faça um programa que leia quanto dinheiro uma pessoa tem e com esse dinheiro
#quantos dolares ela pode comprar. Considerando que U$1,00 == R$3,27

n = float(input('digite o valor em reais: '))

vDolar = n/3.27

print('o valor convertido em dólar é U${:.2f}'.format(vDolar))