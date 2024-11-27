# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input("Qual valor você quer sacar? "))
cedula = 50
cont = 0
while True:
    if valor >= cedula:
        valor-= cedula
        cont+=1
    else:
        if cont !=0:
            print(f'{cont} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula =10
        elif cedula == 10:
            cedula =1
        cont = 0
        if valor == 0:
            break

#####################################################
# c50 = c20 = c10 = c1 = 0

# while valor >= 50:
#     valor-=50
#     c50+=1
# while valor >= 20:
#     valor-=20
#     c20+=1
# while valor >= 10:
#     valor-=10
#     c10+=1
# while valor >= 1:
#     valor-=1
#     c1+=1
    
# if c50 > 0:
#     print(f'{c50} notas de $50')
# if c20 > 0:
#     print(f'{c20} notas de $20')
# if c10 > 0:
#     print(f'{c10} notas de $10')
# if c1 > 0:
#     print(f'{c1} notas de $1')




