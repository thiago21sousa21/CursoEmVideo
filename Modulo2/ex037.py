# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
#  qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

decimal = int(input("Digite um númeor da base decimal: "))

opcao = int(input("""
digite 1: tranforma em binário
digite 2: transforma em octal
digite 3: transforma em hexadecimal
"""))

if opcao == 1:
    print(bin(decimal)[2:])
elif opcao ==2:
    print(oct(decimal)[2:])
elif opcao == 3:
    print(hex(decimal)[2:])
else:
    print("Você não selecionou uma opção válida")