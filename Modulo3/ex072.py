# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
# de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

ate20 = ("zero", 
         "um", "dois", "três", "quatro", "cinco",
         "seis", "sete", "oito", "nove", "dez",
         "onze", "doze", "treze", "catorze", "quinze",
         "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

n =int( input("Digite um número inteiro de zero a 20: "))
while not(0 <= n <= 20):
    n =int( input("Precisa se inteiro de zero a 20! "))
print(f"Você digitou: {ate20[n]}")


