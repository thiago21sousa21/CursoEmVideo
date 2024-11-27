# Um professor quer sortear um dos seus quatro alunos para apagar um quadro
# Faça um programa que ajuda ele lendo o nome deles e escreva o nome do escolhido

from random import choice

a1 = input("nome do primeiro aluno: ")
a2 = input("nome do segundo aluno: ")
a3 = input("nome do terceiro aluno: ")
a4 = input("nome do quarto aluno: ")

lista = [a1, a2, a3, a4]

print(f'O aluno escolhido foi {choice(lista)}')
