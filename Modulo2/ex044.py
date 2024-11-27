# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:

#1 – à vista dinheiro/cheque: 10% de desconto
#2 – à vista no cartão: 5% de desconto
#3 – em até 2x no cartão: preço formal 
#4 – 3x ou mais no cartão: 20% de juros

valor = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
1 – à vista dinheiro/cheque: 10% de desconto
2 – à vista no cartão: 5% de desconto
3 – em até 2x no cartão: preço formal 
4 – 3x ou mais no cartão: 20% de juros
"""))

if forma_de_pagamento ==1:
    valor_final = valor * 0.9
    print(f"à vista dinheiro/cheque: 10% de desconto: {valor_final:.2f}")
elif forma_de_pagamento ==2:
    valor_final = valor * 0.95
    print(f"à vista no cartão: 5% de desconto: {valor_final:.2f}")
elif forma_de_pagamento ==3:  
    print(f"em até 2x no cartão, preço formal: {valor:.2f}")
else: 
    print(f'3x ou mais no cartão, 20% de juros: {valor*1.2:.2f}')