"""Faça um programa que leia o nome completo de uma pessoa e mostre separadamente
o primeiro e o ultimo nome"""

nome_completo = input('Digite seu nome completo: ')

nome_splitado = nome_completo.split(' ')
tamanho = nome_splitado.__len__()

primeiro_nome = nome_splitado[0]
ultimo_nome = nome_splitado[tamanho-1]

print(primeiro_nome)
print(ultimo_nome)