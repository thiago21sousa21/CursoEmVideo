# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação 
# novamente até ter um valor correto.

sexo = ''

while not( sexo == "M" or sexo == "F"):
    sexo = input("Digite seu sexo [M/F]: ").strip().upper()
    if not( sexo == "M" or sexo == "F"):
        print("Você digitou no formato errado, por favor tente novamente")
    else:
        print(f'Você digitou : {sexo}')

