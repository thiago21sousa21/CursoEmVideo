# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = list()
soma_pares = soma_coluna3 = 0
maior_linha2 = 0

for n in range(3):
    linha = list()
    for c in range(3):
        linha.append(input("Digite um valor: "))
    matriz.append(linha)

for idx_linha, l in enumerate(matriz):
    for idx_numero, n in enumerate(l):
        num = int(n)
        if num % 2 == 0:
            soma_pares+=num
        if idx_linha == 2:
            soma_coluna3+=num
        if idx_linha == 1:
            if idx_numero == 0:
                maior_linha2 = num
            else:
                if num > maior_linha2:
                    maior_linha2 = num

        print(f'[{n:^8}]', end=' ')
    print()

print(f'A soma dos números pares é: {soma_pares}')
print(f'A soma dos números da terceira coluna é: {soma_coluna3}')
print(f'O maior valor da segunda linha é: {maior_linha2}')



