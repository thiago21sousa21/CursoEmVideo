# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print("""
Esse programa lê dois números e realiza as operações oferecidas no menu:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
""")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

opc = int(input("Agora digite alguma opção do menu: "))
if(opc ==5):
    print("Saindo..")
while opc !=5 :
    if(opc ==1):
        print(n1+n2)
        opc = int(input("Digite uma nova opção do menu: "))
    elif(opc ==2):
        print(n1*n2)
        opc = int(input("Digite uma nova opção do menu: "))
    elif(opc ==3):
        if (n1>n2):
            print("o maior é o {}".format(n1))
        else:
            print("o maior é o {}".format(n2))                      
        opc = int(input("Digite uma nova opção do menu: "))
    elif(opc ==4):
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        opc = int(input("Digite uma nova opção do menu: "))
    else:
        opc = int(input("Opção inválida tente novamente: "))
        


