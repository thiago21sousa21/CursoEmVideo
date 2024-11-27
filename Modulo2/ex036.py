# Escreva um programa para aprovar o emprestimo bancario para a compra de uma 
# casa. O programa vai perguntar o valor da casa, o salario do comprador e em 
# quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal sabendo que ela não vai poder exceder 30% 
# do salário ou então o empréstimo será negado 

valor_da_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
quantidade_de_prestacoes = int(input("Digite a quantidade de prestações: "))

valor_prestacao = valor_da_casa / quantidade_de_prestacoes

prestacao_sera_aprovada = valor_prestacao <= salario * 0.3

if prestacao_sera_aprovada :
    print("APROVADA!")
else:
    print(f'Não foi aprovada pois o valor da prestação é R${valor_prestacao:.2f} e superou o limite de R${salario*0.3:.2f}')