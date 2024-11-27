#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anoNascimento = int(input("Digite o ano do seu nascimento: "))

ano = date.today().year

idade = ano - anoNascimento

if idade > 18:
    print(f"sua idade é {idade} já deveria ter se alistado há {idade - 18} anos")
elif idade==18:
    print(f"Está no tempo de se alistar! sua idade é {idade}")
else:
    print(f"sua idade é {idade} ainda falta {18-idade} anos para se alistar")