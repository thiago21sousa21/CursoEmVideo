#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por
# dia e R$0,15 por Km rodado.


km_percorrido = float(input('Digite a quantidade de km percorrido: '))
dias_alugado = float(input('Digite a quantidade de dias alugado: '))

valor_a_pagar = 60*dias_alugado + 0.15*km_percorrido

print('O valor total a pagar é: {}'.format(valor_a_pagar))
