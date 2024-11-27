#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print(f"{n1} é o maior e {n2} é menor, O PRIMEIRO É MAIRO")
elif n1==n2:
    print(f"Os dois são iguais ({n1})")
else:
    print(f"{n2} é o maior e {n1} é menor, O SEGUNDO É MAOR")