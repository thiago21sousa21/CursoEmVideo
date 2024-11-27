"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome completo com todas as letras maiusculas
O nome com todas as letras minusculas
Quantas letras ao todo sem  considerar os espaços
Quantas letras tem o primeiro nome"""

nome_completo = input("Digite seu nome completo: ")

nome_maiusculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()
quantidade_espacos = nome_completo.count(" ")
tamanho_nome = nome_completo.__len__()
vetorizado = nome_completo.split()

print("""nome todo maiusculo: {}""".format(nome_maiusculo))
print("""nome todo minusculo: {}""".format(nome_minusculo))
print("""quantidade de letras sem considerar os espaços: {}""".format(tamanho_nome - quantidade_espacos))
print("""quantidade de letras no primeiro nome: {}""".format(vetorizado[0].__len__()))

