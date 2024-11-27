# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

# ler o peso das 5 pessoas com um laço
# ja vamos guardando esse peso em duas variaveis candidatas pra maiores e menores
# se o peso for maior ou menor que o da variavel candidata vai substituindo

maior = 0
menor = 1_000_000
for cont in range(5):
    peso = float(input(f"Digite o peso da {cont+1}º pessoa (kg): "))
    if peso < menor :
        menor = peso 
    if peso > maior:
        maior = peso
        
print(f"O menor peso é {menor}kg e o maior peso é {maior}")