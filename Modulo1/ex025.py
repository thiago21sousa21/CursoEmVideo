"""Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome"""

nome = input('Digite um nome: ').strip()

result = nome.upper().find('SILVA')
print(result != -1)