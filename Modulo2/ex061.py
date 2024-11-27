# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input("Digite o primeiro termo da PA: "))
RAZAO = int(input("Digite a razão da PA: "))

cont = 0
numero_termos = int(input("Digite quantos termos você quer da P.A.: "))

while numero_termos !=0:    
    while cont < numero_termos:
        print(a1 + cont*RAZAO)
        cont += 1
    numero_termos = int(input("Digite outra quantidade de termos dessa PA se quiser parar digite 0: "))
    cont = 0
    