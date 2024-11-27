# Exercício Python 53: Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APÓS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = input("Digite uma frase ou palavra a ser verificaddo se é palíndromo: ")

frase = frase.split(" ")
frase = "".join(frase)

reverso = ''

for c in range(len(frase)-1, -1,-1):
    reverso += frase[c]

if frase == reverso:
    print("SIM é um palídromo")
else:
    print('Não é um palídromo') 

