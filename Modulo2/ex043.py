# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input("Qual seu peso em kg? "))
altura = float(input("Qual sua altura em m? "))

imc = peso/altura**2

print(f"Seu imc é : {imc:.2f} ", end='')
if imc < 18.5:
    print("abaixo do peso")
elif imc <25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Acima do peso")