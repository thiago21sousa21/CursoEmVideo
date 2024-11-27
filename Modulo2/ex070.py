# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = mais_de_1000 = mais_barato_preco = 0
mais_barato_nome = ''
while True:
    nome = (input("Digite o nome do produto a ser cadastrado: "))
    preco = float(input("Digite o o preço do produto a ser cadastrado: "))
    
    total+= preco
    if preco > 1000:
        mais_de_1000+=1
    if mais_barato_preco == 0 or preco < mais_barato_preco:
        mais_barato_preco = preco
        mais_barato_nome = nome
    
    continuar = input("Cadastrar mais um produto[S/N]? ").strip().upper()[0]
    if continuar == 'N':
        break
    
print(f'''O total da compra deu {total}
      {mais_de_1000} custaram mais de R$1000
      e o produto mais barato foi {mais_barato_nome}''')