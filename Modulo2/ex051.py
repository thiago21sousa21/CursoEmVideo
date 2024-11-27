# Exercício Python 51: Desenvolva um programa que leia o primeiro termo 
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input("Digite o primeiro termo da PA: "))
RAZAO = int(input("Digite a razão da PA: "))

for n in range(10):
    print(a1 + RAZAO*(n))