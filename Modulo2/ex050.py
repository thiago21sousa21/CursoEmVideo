# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a 
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma=0
for c in range(6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        soma += n
print(soma)