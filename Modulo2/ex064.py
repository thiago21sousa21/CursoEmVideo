# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
soma = 0
n = 0
while n != 999:
    n = int(input("Digite um número a ser somado a uma sequencia para parar digite 999: "))
    if n != 999:
        cont+=1
        soma+=n
print(f"foram digitados {cont} números e a soma de todos eles dá {soma}")

