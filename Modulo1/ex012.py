#faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de
#desconto

preco = float(input('digite o preço: '))

preco_com_desconto = preco - preco*0.05

print('o valor com desconto é {}'.format(preco_com_desconto))