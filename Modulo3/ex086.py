# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e 
# preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.

matriz = list()

for n in range(3):
    linha = list()
    for c in range(3):
        linha.append(input("Digite um valor: "))
    matriz.append(linha)

for n in range(3):
    print(matriz[n])

