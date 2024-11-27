# Exercício Python 076: Crie um programa que tenha uma tupla única 
# com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tabela_precos = (
    'salgado', 5,
    'bomba', 4,
    'coxinha', 6,
    'suco', 2
)

for d in range(0,len(tabela_precos)-1, 2):
    print(f'{tabela_precos[d]}-------${tabela_precos[d+1]}')
    

